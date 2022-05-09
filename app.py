from flask import Flask, request, render_template, redirect, url_for
import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('action1') == 'START':
            #redirect(url_for(q1.html))
            return render_template('q1.html')
        elif request.form.get('action2') == 'Feedback':
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
            print("maybe")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

@app.route('/spotifycallback', methods=["GET", "POST"])
def spotifycallback():
    if request.method == 'POST':
        access_token = request.args.get('access_token')
        refresh_token = request.args.get('refresh_token')
        expires_in = request.args.get('expires_in')
        tokens = {'access_token': access_token, 'refresh_token': refresh_token, 'expires_in':expires_in}
        return tokens
    elif request.method == 'GET':
        code = request.args.get('code')
        state = request.args.get('state')
        auth = {'code': code, 'state': state}
        authorization = requests.post(
                                    "https://accounts.spotify.com/api/token",
                                    auth=(CLIENT_ID, CLIENT_SECRET),
                                    data={
                                        "grant_type": "authorization_code",
                                        "code": code,
                                        "redirect_uri": SPOTIFY_REDIRECT_URI,
                                    },        
                                )
        a = authorization.json()
        access_token = a['access_token']
        refresh_token = a['refresh_token']
        expires_in = a['expires_in']
        q = {'access_token': access_token, 'refresh_token': refresh_token, 'expires_in ': expires_in }
        return q
    else :
        return "yes"

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


"""
    if answer =='ME':
        return redirect(url_for('login'))
    elif answer = "OTHER":
        
    else:
        return redirect(url_for('question3'))
"""
if __name__ == '__main__':
    app.run(debug = True)