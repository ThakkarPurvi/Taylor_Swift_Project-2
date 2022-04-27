from application import app, db
from application.models import UserProfile, Song
from flask import request, Response, jsonify, render_template, redirect, url_for
import os

#Create User Profile
@app.route('/create/userprofile', methods=["POST"])
def create_userprofile():
    json = request.json
    new_userprofile = userprofile(
        name = json["name"]
    )
    db.session.add(new_userprofile)
    db.session.commit()
    return f"UserProfile '{new_userprofile.name}' added to database"

#Create Song
@app.route('/create/song/<int:userprofile_id>', methods=["POST"])
def create_song(userprofile_id):
    json = request.json
    new_song = Song(
        song_category = json["song_category"],
        userprofile_id = userprofile_id,
        song_description = json["song_description"]
    )
    db.session.add(new_song)
    db.session.commit()
    return f"Song '{new_song.name}' added to database"

#Get all User Profiles
@app.route('/get/allUserProfiles', methods=["GET"])
def get_all_UserProfile():
    all_userprofiles = UserProfile.query.all()
    json = {"userprofiles": []}
    for userprofile in all_userprofiles:
        songs = []
        for song in userprofile.songs:
            songs.append(
                {
                    "id": song.id,
                    "song_category": song.song_category,
                    "song_id": song.userprofile_id,
                    "song_description": song.song_description
                }
            )
        json["userprofiles"].append(
            {
                "id": userprofile.id,
                "name": userprofile.name,
                "songs": songs
            }
        )
    return jsonify(json)

@app.route('/get/allSongs', methods=["GET"])
def get_all_songs():
    all_songs = UserProfile.query.all()
    json = {"songs": []}
    for song in all_songs:
        json["songs"].append(
            {
                "id": song.id,
                "song_category": song.song_category,
                "userprofile_id": song.userprofile_id,
                "song_description": song.song_description
            }
        )
    return jsonify(json)

@app.route('/get/UserProfile/<int:id>', methods=["GET"])
def get_userprofile(id):
    userprofile = UserProfile.query.get(id)
    return jsonify(
        {
            "id": userprofile.id,
            "name": userprofile.name
        }
    )

@app.route('/get/UserProfile/<int:id>/songs', methods=["GET"])
def get_songs(id):
    songs = UserProfile.query.get(id).songs
    json = {"songs": []}
    for song in songs:
        json["songs"].append(
            {
                "id": song.id,
                "song_category": song.song_category,
                "userprofile_id": song.userprofile_id,
                "song_description": song.song_description
            }
        )
    return jsonify(json)

#Update userprofile
@app.route('/update/userprofile/<int:id>', methods=["PUT"])
def update_userprofile(id):
    data = request.json
    userprofile = UserProfile.query.get(id)
    userprofile.name = data["name"]
    db.session.commit()
    return f"UserProfile '{userprofile.name}' updated successfully"

#Delete userprofile
@app.route('/delete/userprofile/<int:id>', methods=["DELETE"])
def delete_userprofile(id):
    userprofile = UserProfile.query.get(id)
    db.session.delete(userprofile)
    db.session.commit()
    return f"UserProfile '{userprofile.name}' deleted successfully"

#Update Song
@app.route('/update/song/<int:id>', methods=["PUT"])
def update_song(id):
    data = request.json
    song = Song.query.get(id)
    song.song_description = data["song_description"],
    song.song_category = data["song_category"]
    db.session.commit()
    return f"Song '{song.name}'updated successfully"

#Delete Song
@app.route('/delete/song/<int:id>', methods=["DELETE"])
def delete_song(id):
    song = Song.query.get(id)
    db.session.delete(song)
    db.session.commit()
    return f"Song '{song.name}' deleted successfully"