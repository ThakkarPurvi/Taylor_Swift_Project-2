from flask import Flask, request, render_template, redirect, url_for
import requests
import json
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN
from SpotifyApi import Spotify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('action1') == 'START':
            return render_template('q1.html')
        elif request.form.get('action2') == 'Feedback':
            return render_template('feedback.html')
        elif request.form.get('action3') == 'Spotify':
            auth_response = requests.get(AUTH_URL, {
                                                    'response_type': 'code',
                                                    'client_id': CLIENT_ID,
                                                    'scope': SCOPE,
                                                    'redirect_uri': SPOTIFY_REDIRECT_URI,
                                                    'state': 'state'
                                                })

            print(auth_response.url, type(auth_response.url))
            return redirect(auth_response.url)
        else:
            print("something wrong")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

@app.route('/spotifycallback', methods=["GET", "POST"])
def spotifycallback():
    if request.method == 'GET':
        code = request.args.get('code')
        state = request.args.get('state')
        auth_code = {'code': code, 'state': state}
        spotify = Spotify()
        auth_spotify_token = spotify.get_token(code)
        spotify_token = auth_spotify_token['access_token']
        user_id = spotify.get_user_id(auth_spotify_token['access_token'])
        playlist_id = spotify.get_playlist_id(user_id, spotify_token)
        song_uri = spotify.get_song_uri()
        spotify.add_song(song_uri, playlist_id, spotify_token)
        return "check your spotify"
    else :
        return render_template("index.html")

@app.route('/q1', methods=["GET"])
def test():
    return(request.args.get("name"))

@app.route('/q2', methods=["GET"])
def handle_question2():
    pass

@app.route('/q3', methods=["GET"])
def handle_question3():
    pass

@app.route('/q4', methods=["GET"])
def handle_question4():
    pass


@app.route('/playlist', methods=['GET', 'POST'])
def add_playlist_spotify():
    if request.method == 'POST':
        if request.form.get('action1') == 'Feedback':
            return render_template('feedback.html')
        elif request.form.get('action2') == 'Spotify':
            print("here")
            auth_response = requests.get(AUTH_URL, {
                                                    'response_type': 'code',
                                                    'client_id': CLIENT_ID,
                                                    'scope': SCOPE,
                                                    'redirect_uri': SPOTIFY_REDIRECT_URI,
                                                    'state': 'state'
                                                })

            return redirect(auth_response.url)
        else:
            print("Something got wrong")
    elif request.method == 'GET':
        # displya playlist
        return render_template('playlist.html')
    return "ok"

if __name__ == '__main__':
    app.run(debug = True)