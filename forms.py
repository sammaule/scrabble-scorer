from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class NewGameForm(FlaskForm):
    num_players = IntegerField('Number of Players',
                               validators=[DataRequired(),
                                           NumberRange(min=2, max=4, message='2 - 4 players only.')])
    player_1_name = StringField('Player 1 Name',
                                validators=[])
    player_2_name = StringField('Player 2 Name',
                                validators=[])
    player_3_name = StringField('Player 3 Name',
                                validators=[])
    player_4_name = StringField('Player 4 Name',
                                validators=[])
    submit = SubmitField('Start Game')


class MidGameForm(FlaskForm):
    player_1_score = IntegerField('Player 1 score:',
                                  validators=[DataRequired()])
    player_2_score = IntegerField('Player 2 score:',
                                  validators=[DataRequired()])
    player_3_score = IntegerField('Player 1 score:',
                                  validators=[DataRequired()])
    player_4_score = IntegerField('Player 4 score:',
                                  validators=[DataRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')
