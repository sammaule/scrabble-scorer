from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class NewGameForm(FlaskForm):
    num_players = SelectField('Number of Players',
                              validators=[DataRequired()],
                              choices=[('2', '2'), ('3', '3'), ('4', '4')])
    player_1_name = StringField('Player 1 Name',
                                validators=[])
    player_2_name = StringField('Player 2 Name',
                                validators=[])
    player_3_name = StringField('Player 3 Name',
                                validators=[])
    player_4_name = StringField('Player 4 Name',
                                validators=[])
    submit = SubmitField('Start Game')


class TwoPlayerGameForm(FlaskForm):

    player_1_score = IntegerField('Player 1 score:',
                                  validators=[DataRequired()])
    player_2_score = IntegerField('Player 2 score:',
                                  validators=[DataRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class ThreePlayerGameForm(FlaskForm):

    player_1_score = IntegerField('Player 1 score:',
                                  validators=[DataRequired()])
    player_2_score = IntegerField('Player 2 score:',
                                  validators=[DataRequired()])
    player_3_score = IntegerField('Player 3 score:',
                                  validators=[DataRequired()])

    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class FourPlayerGameForm(FlaskForm):

    player_1_score = IntegerField('Player 1 score:',
                                  validators=[DataRequired()])
    player_2_score = IntegerField('Player 2 score:',
                                  validators=[DataRequired()])
    player_3_score = IntegerField('Player 3 score:',
                                  validators=[DataRequired()])
    player_4_score = IntegerField('Player 4 score:',
                                  validators=[DataRequired()])

    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')