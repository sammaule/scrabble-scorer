from flask import render_template, url_for, flash, redirect, session, request
from scrabblescorer import app, db
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


#TODO: Send players to home page if a session hasn't started
@app.route("/enter_names", methods=['GET', 'POST'])
def enter_names():
    # Get the number of players in the game and display the correct form
    num_players = session.get('num_players', None)
    if num_players == '2':
        form = TwoPlayerNameForm()
    elif num_players == '3':
        form = ThreePlayerNameForm()
    elif num_players == '4':
        form = FourPlayerNameForm()

    # Add the player names and starting scores to the session
    if form.validate_on_submit():
        players = []
        for field in form:
            if field.type == 'StringField':
                players.append(field.data)
        # Get session players and scores
        session['player_scores'] = [list(a) for a in zip(players, [0] * len(players))]
        flash('Starting Game!', 'success')
        return redirect(url_for('game'))
    # TODO: remove num_players from output here when all working.
    return render_template('enter_names.html', form=form, num_players=num_players)


# Mid game class
@app.route("/game", methods=['GET', 'POST'])
def game():
    # Get the number of players in the game and display the correct form
    num_players = session.get('num_players', None)
    # Get the current players and scores
    player_scores = session.get('player_scores', None)
    if num_players == '2':
        form = TwoPlayerGameForm()
    elif num_players == '3':
        form = ThreePlayerGameForm()
    elif num_players == '4':
        form = FourPlayerGameForm()

    # Add latest turn scores to the database
    if form.validate_on_submit():
        # Get only the score fields
        fields = [field for field in form if field.type == 'IntegerField']
        # Update scores
        new_scores = []
        for field in fields:
            new_scores.append(field.data)
        old_scores = [i[1] for i in player_scores]
        new_scores = [old_score + latest_score for old_score, latest_score in zip(old_scores, new_scores)]
        players = [i[0] for i in player_scores]
        player_scores = [list(a) for a in zip(players, new_scores)]
        # Checks which button was pressed
        if form.submit.data:
            session['player_scores'] = player_scores
            flash('Scores updated.', 'success')
            return redirect(url_for('game'))
        elif form.end_game.data:
            session['player_scores'] = player_scores
            return redirect(url_for('final_scores'))
    return render_template('game.html', form=form, num_players=num_players, player_scores=player_scores)


# final scores
@app.route("/final_scores", methods=['GET', 'POST'])
def final_scores():
    player_scores = session.get('player_scores', None)
    form = FinalScoreForm()
    if form.validate_on_submit():
        # Drop session values
        session.pop('player_scores', None)
        session.pop('num_players', None)
        return redirect(url_for('start_game'))
    return render_template('final_scores.html', form=form, player_scores=player_scores)
