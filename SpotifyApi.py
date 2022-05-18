import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL, SPOTIFY_REDIRECT_URI
from requests.structures import CaseInsensitiveDict


class Spotify():
    def __init__(self):
        self.token_url = TOKEN_URL
        self.artist = "Taylor Swift"
    
    def get_token(self, code):
        authorization = requests.post(
                                    "https://accounts.spotify.com/api/token",
                                    auth=(CLIENT_ID, CLIENT_SECRET),
                                    data={
                                        "grant_type": "authorization_code",
                                        "code": code,
                                        "redirect_uri": SPOTIFY_REDIRECT_URI,
                                    },        
                                )
        auth_token = authorization.json()
        if authorization.status_code == 200:
            access_token =  auth_token['access_token']
            refresh_token =  auth_token['refresh_token']
            expires_in =  auth_token['expires_in']
            auth_spotify_token = {'access_token': access_token, 'refresh_token': refresh_token, 'expires_in ': expires_in }
            return auth_spotify_token
        else:
            return None
    
    def get_user_id(self, spotify_auth):
        url = "https://api.spotify.com/v1/me"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(spotify_auth)
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp_json = resp.json()
            user_id = resp_json["id"]
            return user_id
        else:
            return None
    
    def get_song_uri(self, song, spotify_token):
        song_name = song
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                    song_name,
                    self.artist
                )
        response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        if response.status_code == 200:
            song_uri = response_json["tracks"]["items"][0]["uri"]
            return song_uri
        else:
            return None
        
    def get_playlist_id(self, user_id, spotify_token):
        request_body = json.dumps({
            "name": "Taylor Swift Playlist",
            "description": "Python Project 2 CFG",
            "public": False
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
        response = requests.post(
                    query,
                    data=request_body,
                    headers={
                        "Accept" : "application/json",
                        "Content-Type": "application/json",
                        "Authorization": "Bearer {}".format(spotify_token)
                    }
                )
        response_json = response.json()
        if (response.status_code == 200) or (response.status_code == 201):
            playlist_id = response_json["id"]
            return playlist_id
        else:
            return None
    
    def add_song(self, song, playlist_id, spotify_token):
        url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks?position=0&uris=" + song
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(spotify_token)
        headers["Content-Length"] = "0"
        resp = requests.post(url, headers=headers)


