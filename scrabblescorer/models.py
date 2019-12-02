from scrabblescorer import db


class Player(db.Model):
    """database for storing score information"""
    id = db.Column(db.Integer, primary_key=True)
    # todo set length limit on names in field entry
    player = db.Column(db.String(20), nullable=False)
    scores = db.relationship('Score', backref='player')

    # TODO: count the turns taken each time
    def __repr__(self):
        return f"Player('{self.player}')"


class Score(db.Model):
    """database for storing score information"""
    id = db.Column(db.Integer, primary_key=True)
    # TODO: count the turns taken each time
    score = db.Column(db.Integer, nullable=False, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))

    def __repr__(self):
        return f"Score('{self.player_id}', '{self.score}')"
