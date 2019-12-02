"""Defines the database structure for the scorer"""
from scrabblescorer import db


class Player(db.Model):
    """database for storing score information"""
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Player('{self.player}', '{self.score}')"
