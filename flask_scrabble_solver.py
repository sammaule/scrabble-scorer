from flask import Flask, render_template, url_for, flash, redirect

from forms import NewGameForm, MidGameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bfgsb4321fdsdfs42hdhfjd82898ba245'

# Pre game class
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def start_game():
	form = NewGameForm()
	if form.validate_on_submit():
		flash('Starting Game!', 'success')
		return redirect(url_for('game'))
	return render_template('start_game.html', form=form)

# Mid game class
@app.route("/game", methods=['GET', 'POST'])
def game():
	form = MidGameForm()
	return render_template('game.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)
