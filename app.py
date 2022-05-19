from flask import Flask, request, render_template, redirect, url_for
import requests
import json
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SPOTIFY_REDIRECT_URI
from SpotifyApi import Spotify
from Taylor_questions_stored import questions_taylor, options_taylor
from DatabaseConnection import DatabaseConnection
from DatabaseManager import DatabaseManager
from Model import Model


app = Flask(__name__)

songs = []

@app.route('/', methods=['GET', 'POST'])
def start_playlist():
    if request.method == 'POST':
        if request.form.get('action1') == 'START':
            print("START")
            return redirect(url_for('handle_question1'))
        elif request.form.get('action2') == 'Feedback':
            return render_template('feedback.html')
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

@app.route('/q1/', methods=['GET','POST'])
def handle_question1():
    if request.method == 'GET':
        question1 = questions_taylor[0]
        options= options_taylor[0].items()
        return render_template("q1.html",question1 = question1, options = options)
    elif request.method == 'POST':
        if request.form.get('1') == '1.':
            model = Model()
            global songs 
            songs = model.get_songs(None)
            print(songs)
            return render_template("playlist.html", songs = songs)
        elif request.form.get('2') == '2.':
            return redirect(url_for('handle_question2'))
        else:
            return redirect(url_for('start_playlist'))
        
@app.route('/q2/', methods=['GET','POST'])
def handle_question2():
    if request.method == 'GET':
        index = 1
        question2 = questions_taylor[index]
        options= options_taylor[index].items()
        return render_template("q2.html",question2 = question2, options = options)
    elif request.method == 'POST':
        answer = {"subject": None}
        if request.form.get("ME") == "ME":
            answer["subject"] = "ME"
            return redirect(url_for('handle_question4', answer = answer))
        elif request.form.get('OTHER') == "OTHER":
            return redirect(url_for('handle_question3'))
        else:
            return redirect(url_for('start_playlist'))
    return redirect(url_for('start_playlist'))

@app.route('/q3/', methods=['GET','POST'])
def handle_question3():
    index = 2
    if request.method == 'GET':
        question3 = questions_taylor[index]
        options= options_taylor[index].items()
        return render_template("q3.html",question3 = question3, options = options)
    elif request.method == 'POST':
        answer = {"subject": None}
        answer["subject"]= request.form.get('action3')
        return redirect(url_for('handle_question4', answer = answer))
    return redirect(url_for('start_playlist'))

@app.route('/q4/<answer>/', methods=['GET','POST'])
def handle_question4(answer):
    index = 3
    if request.method == 'GET':
        question4 = questions_taylor[index]
        options= options_taylor[index].items()
        url_question4_arg = "http://127.0.0.1:5000/q4/" + answer + "/"
        return render_template("q4.html",question4 = question4, options = options, url_question4_arg=url_question4_arg)
    elif request.method == 'POST':
        vibe = request.form.get('action4')
        json_acceptable_string = answer.replace("'", "\"")
        answer = json.loads(json_acceptable_string)          
        answer["vibe"] = vibe
        model = Model()
        global songs 
        songs = model.get_songs(answer)
        return render_template("playlist.html", songs = songs)

@app.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("feedback.html")

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
        for song in songs:
            song_uri = spotify.get_song_uri(song, spotify_token)
            spotify.add_song(song_uri, playlist_id, spotify_token)
            print(user_id)
        return "check your spotify"
    else :
        return render_template("index.html")

@app.route('/playlist', methods=['GET', 'POST'])
def add_playlist_spotify():
    if request.method == 'POST':
        if request.form.get('action1') == 'Feedback':
            return render_template('feedback.html')
        elif request.form.get('action2') == 'Spotify':
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
        return render_template('playlist.html')
    return render_template('playlist.html')

if __name__ == '__main__':
    app.run(debug = True)