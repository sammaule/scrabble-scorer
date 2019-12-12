from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired


class NewGameForm(FlaskForm):
    """Form to get the number of players."""
    num_players = SelectField('Number of Players',
                              validators=[DataRequired()],
                              choices=[('2', '2'), ('3', '3'), ('4', '4')])
    submit = SubmitField('Next')


class TwoPlayerGameForm(FlaskForm):
    """Form to get 2 players scores"""
    player_1_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class ThreePlayerGameForm(FlaskForm):
    """Form to get 3 players scores"""
    player_1_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField('turn:',
                                  validators=[InputRequired()])

    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class FourPlayerGameForm(FlaskForm):
    """Form to get 4 players scores"""
    player_1_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    player_4_score = IntegerField('turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


# Forms to get player names
class TwoPlayerNameForm(FlaskForm):
    """Form to get 2 players names"""
    player_1_name = StringField('Player 1 name:',
                                  validators=[DataRequired()])
    player_2_name = StringField('Player 2 name:',
                                  validators=[DataRequired()])
    submit = SubmitField('Start Game')


class ThreePlayerNameForm(FlaskForm):
    """Form to get 3 players names"""
    player_1_name = StringField('Player 1 name:',
                                  validators=[DataRequired()])
    player_2_name = StringField('Player 2 name:',
                                  validators=[DataRequired()])
    player_3_name = StringField('Player 3 name:',
                                  validators=[DataRequired()])
    submit = SubmitField('Start Game')


class FourPlayerNameForm(FlaskForm):
    """Form to get 4 players names"""
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


class FinalScoreForm(FlaskForm):
    """Form to get the number of players."""
    submit = SubmitField('New Game')