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


class TwoPlayerGameForm(FlaskForm):
    player_1_score = IntegerField(f'{db.session.query(Player).first().player} turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField(f'{db.session.query(Player).offset(1).first().player} turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class ThreePlayerGameForm(FlaskForm):
    player_1_score = IntegerField(f'{db.session.query(Player).first().player} turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField(f'{db.session.query(Player).offset(1).first().player} turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField(f'{db.session.query(Player).offset(2).first().player} turn:',
                                  validators=[InputRequired()])
    submit = SubmitField('Update Scores')
    end_game = SubmitField('End Game')


class FourPlayerGameForm(FlaskForm):
    player_1_score = IntegerField(f'{db.session.query(Player).first().player} turn:',
                                  validators=[InputRequired()])
    player_2_score = IntegerField(f'{db.session.query(Player).offset(1).first().player} turn:',
                                  validators=[InputRequired()])
    player_3_score = IntegerField(f'{db.session.query(Player).offset(2).first().player} turn:',
                                  validators=[InputRequired()])
    player_4_score = IntegerField(f'{db.session.query(Player).offset(3).first().player} turn:',
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