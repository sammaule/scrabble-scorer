from flask import render_template, url_for, flash, redirect, session, request
from sqlalchemy import func
from scrabblescorer import app, db
from scrabblescorer.models import Score, Player
from scrabblescorer.forms import TwoPlayerGameForm, ThreePlayerGameForm, FourPlayerGameForm, NewGameForm,\
    TwoPlayerNameForm, ThreePlayerNameForm, FourPlayerNameForm

# Pre game class
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def start_game():
    form = NewGameForm()
    # Save the number of players to be accessed elsewhere
    session['num_players'] = request.form.get('num_players')
    if form.validate_on_submit():
        db.drop_all()
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
        player_1 = Player(player=form.player_1_name.data)
        player_2 = Player(player=form.player_2_name.data)
        db.session.add(player_1)
        db.session.add(player_2)

        if num_players == '3' or num_players == '4':
            player_3 = Player(player=form.player_3_name.data)
            db.session.add(player_3)

        if num_players == '4':
            player_4 = Player(player=form.player_4_name.data)
            db.session.add(player_4)

        db.session.commit()
        flash('Starting Game!', 'success')
        return redirect(url_for('game'))
    return render_template('enter_names.html', form=form)

# Mid game class
@app.route("/game", methods=['GET', 'POST'])
def game():
    num_players = session.get('num_players', None)

    # Get the scores to display
    sum_scores = []
    sum_scores.append(db.session.query(func.sum(Score.score)).join(Player).filter_by(id=1).scalar())
    sum_scores.append(db.session.query(func.sum(Score.score)).filter_by(id=2).scalar())
    if num_players == '2':
        form = TwoPlayerGameForm()
    elif num_players == '3':
        sum_scores.append(db.session.query(func.sum(Score.score)).filter_by(player_id=3).scalar())
        form = ThreePlayerGameForm()
    elif num_players == '4':
        sum_scores.append(db.session.query(func.sum(Score.score)).filter_by(player_id=3).scalar())
        sum_scores.append(db.session.query(func.sum(Score.score)).filter_by(player_id=4).scalar())
        form = FourPlayerGameForm()

    # Add latest turn scores to the database
    if form.validate_on_submit():
        score_1 = Score(score=form.player_1_score.data, player_id=1)
        score_2 = Score(score=form.player_2_score.data, player_id=2)
        db.session.add(score_1)
        db.session.add(score_2)
        if num_players == '3' or num_players == '4':
            score_3 = Score(score=form.player_3_score.data, player_id=3)
            db.session.add(score_3)
        if num_players == '4':
            score_4 = Score(score=form.player_4_score.data, player_id=4)
            db.session.add(score_4)
        db.session.commit()

        # Checks which button was pressed
        if form.submit.data:
            flash('Scores updated.', 'success')
            return redirect(url_for('game'))
        elif form.end_game.data:
            flash('Game ended. The winner was [FIXME].', 'success')
            return redirect(url_for('start_game'))
    # TODO: Clear the database when game ends/starts
    return render_template('game.html', form=form, num_players=num_players, sum_scores=sum_scores)