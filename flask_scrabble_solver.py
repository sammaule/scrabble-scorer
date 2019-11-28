from flask import Flask, render_template, url_for, flash, redirect, session, request

from forms import NewGameForm, TwoPlayerGameForm, ThreePlayerGameForm, FourPlayerGameForm

# TODO: Build database to store all names and scores?
with open('secret_code.txt','r') as f:
    message = f.read()

app = Flask(__name__)
app.config['SECRET_KEY'] = message

# Pre game class
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def start_game():
	form = NewGameForm()
	# Save the number of players to be accessed elsewhere
	session['num_players'] = request.form.get('num_players')
	player_names = []
	for field in form:
		if field.type == 'StringField':
			name = request.form.get(field)
			player_names.append(name)
	session['player_names'] = player_names
	if form.validate_on_submit():
		flash('Starting Game!', 'success')
		return redirect(url_for('game'))
	return render_template('start_game.html', form=form)


# Mid game class
@app.route("/game", methods=['GET', 'POST'])
def game():
	num_players = session.get('num_players', None)
	player_names = session.get('player_names', None)
	# TODO: Display the names of the players in the game screen
	if num_players == '2':
		form = TwoPlayerGameForm()
	elif num_players == '3':
		form = ThreePlayerGameForm()
	elif num_players == '4':
		form = FourPlayerGameForm()
	# TODO Store and update the scores as the game progresses
	if form.validate_on_submit():
		# Checks which button was pressed
		if form.submit.data:
			flash('Scores updated.', 'success')
			return redirect(url_for('game'))
		elif form.end_game.data:
			# TODO: Ask user to update scores for final time
			flash('Game ended. Enter final tile values for all players.', 'success')
			return redirect(url_for('game'))
	return render_template('game.html', form=form, num_players=num_players, player_names=player_names)

if __name__ == '__main__':
	app.run(debug=True)
