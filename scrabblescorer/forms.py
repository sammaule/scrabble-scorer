from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired
from scrabblescorer import db
from scrabblescorer.models import Score, Player


class NewGameForm(FlaskForm):
    num_players = SelectField('Number of Players',
                              validators=[DataRequired()],
                              choices=[('2', '2'), ('3', '3'), ('4', '4')])
    submit = SubmitField('Next')

# Potential query to get player names
# {db.session.query(Player).first().player}

class TwoPlayerGameForm(FlaskForm):
    player_1_score = IntegerField('Player 1 turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('Player 2 turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class ThreePlayerGameForm(FlaskForm):
    player_1_score = IntegerField('Player 1 turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('Player 2 turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField('Player 3 turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class FourPlayerGameForm(FlaskForm):
    player_1_score = IntegerField('Player 1 turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('Player 2 turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField('Player 3 turn:',
                                  validators=[InputRequired()])
    player_4_score = IntegerField('Player 4 turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


# Forms to get player names
class TwoPlayerNameForm(FlaskForm):
    player_1_name = StringField('Player 1 name:',
                                  validators=[DataRequired()])
    player_2_name = StringField('Player 2 name:',
                                  validators=[DataRequired()])
    submit = SubmitField('Start Game')


class ThreePlayerNameForm(FlaskForm):
    player_1_name = StringField('Player 1 name:',
                                  validators=[DataRequired()])
    player_2_name = StringField('Player 2 name:',
                                  validators=[DataRequired()])
    player_3_name = StringField('Player 3 name:',
                                  validators=[DataRequired()])
    submit = SubmitField('Start Game')


class FourPlayerNameForm(FlaskForm):
    player_1_name = StringField('Player 1 name:',
                                  validators=[DataRequired()])
    player_2_name = StringField('Player 2 name:',
                                  validators=[DataRequired()])
    player_3_name = StringField('Player 3 name:',
                                  validators=[DataRequired()])
    player_4_name = StringField('Player 4 name:',
                                  validators=[DataRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')