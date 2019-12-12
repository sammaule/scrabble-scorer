from flask import render_template, url_for, flash, redirect, session, request
from scrabblescorer import app, db
from scrabblescorer.models import Player
from scrabblescorer.forms import TwoPlayerGameForm, NewGameForm, TwoPlayerNameForm, \
    ThreePlayerGameForm, FourPlayerGameForm, ThreePlayerNameForm, FourPlayerNameForm, FinalScoreForm


# Pre game class
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def start_game():
    db.drop_all()
    form = NewGameForm()
    # Save the number of players to be accessed elsewhere
    session['num_players'] = request.form.get('num_players')
    if form.validate_on_submit():
        db.create_all()
        return redirect(url_for('enter_names'))
    return render_template('start_game.html', form=form)


@app.route("/enter_names", methods=['GET', 'POST'])
def enter_names():
    num_players = session.get('num_players', None)
    if num_players == '2':
        form = TwoPlayerNameForm()
    elif num_players == '3':
        form = ThreePlayerNameForm()
    elif num_players == '4':
        form = FourPlayerNameForm()

    if form.validate_on_submit():
        # Add player names to the database
        players = []
        for field in form:
            if field.type == 'StringField':
                players.append({field.data: 0})
                player = Player(player=field.data, score=0)
                db.session.add(player)
        # Get session players and scores
        session['session_players'] = players
        db.session.commit()
        flash('Starting Game!', 'success')
        return redirect(url_for('game'))
    return render_template('enter_names.html', form=form)


# Mid game class
@app.route("/game", methods=['GET', 'POST'])
def game():
    num_players = session.get('num_players', None)
    if num_players == '2':
        form = TwoPlayerGameForm()
    elif num_players == '3':
        form = ThreePlayerGameForm()
    elif num_players == '4':
        form = FourPlayerGameForm()

    players = Player.query.all()
    session_players = session.get('players', None)
    # Add latest turn scores to the database
    if form.validate_on_submit():
        fields = [field for field in form if field.type == 'IntegerField']
        for field, player, session_player in zip(fields, players, session_players):
            player.score += field.data
            session_player += field.data
        db.session.commit()

        # Checks which button was pressed
        if form.submit.data:
            flash('Scores updated.', 'success')
            return redirect(url_for('game'))
        elif form.end_game.data:
            return redirect(url_for('final_scores'))
    return render_template('game.html', form=form, players=players, num_players=num_players,
                           session_players=session_players)


# final scores
@app.route("/final_scores", methods=['GET', 'POST'])
def final_scores():
    players = Player.query.all()
    form = FinalScoreForm()
    if form.validate_on_submit():
        return redirect(url_for('start_game'))
    return render_template('final_scores.html', form=form, players=players)
