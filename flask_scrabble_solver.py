from flask import Flask, render_template, url_for
from forms import NewGameForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bfgsb4321fdsdfs42hdhfjd82898ba245'

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
	form = NewGameForm()
	return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)