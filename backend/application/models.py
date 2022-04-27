from application import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    songs = db.relationship("Song", backref="userprofile")


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_category = db.Column(db.String(50), nullable=False)
    song_description = db.Column(db.String(500), nullable=False)

    userprofile_id = db.Column(db.Integer, db.ForeignKey("user_profile.id"), nullable=False)