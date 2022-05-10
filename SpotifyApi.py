import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN
from requests.structures import CaseInsensitiveDict


class Spotify():
    def __init__(self):
        self.token_url = TOKEN_URL
        self.artist = "Taylor Swift"
        self.userID = "yj46x5ujbzvzvwlxfidiwxwt8"
        self.songs_name = ["The Other Side Of The Door (Taylor's Version)", "Tell Me Why (Taylor's Version)","The Last Time (feat. Gary Lightbody of Snow Patrol) (Taylor's Version)"]

    def __get_token2(self):
        token_response = requests.post(self.token_url, {
                                                'grant_type': 'client_credentials',
                                                'client_id': CLIENT_ID,
                                                'client_secret': CLIENT_SECRET,
                                                })

        # convert the response to JSON
        token_response_data = token_response.json()
        # save the access token
        spotify_token = token_response_data['access_token']
        return spotify_token
    
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
        # maybe check reponse 200 ??
        access_token =  auth_token['access_token']
        refresh_token =  auth_token['refresh_token']
        expires_in =  auth_token['expires_in']
        auth_spotify_token = {'access_token': access_token, 'refresh_token': refresh_token, 'expires_in ': expires_in }
        return auth_spotify_token 
    
    def get_user_id(self, spotify_auth):
        url = "https://api.spotify.com/v1/me"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(spotify_auth)
        resp = requests.get(url, headers=headers)
        print(resp.status_code)
        if resp.status_code == 200:
            resp_json = resp.json()
            user_id = resp_json["id"]
            print(user_id)
            return user_id
    
    def get_song_uri(self):
        spotify_token = self.__get_token2()
        song_name3 = "The Very First Night (Taylor's Version) (From The Vault)"
        song_name2 = self.songs_name[0]
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                    song_name2,
                    self.artist
                )
        response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        print(response.status_code)
        if response.status_code == 200:
            song_uri = response_json["tracks"]["items"][0]["uri"]
            return song_uri
        
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
        playlist_id = response_json["id"]
        print("playlist id: ", playlist_id)
        return playlist_id
    
    def add_song(self, songs, playlist_id, spotify_token):
        url = "https://api.spotify.com/v1/playlists/"+playlist_id+"/tracks?position=0&uris="+songs
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(spotify_token)
        headers["Content-Length"] = "0"
        resp = requests.post(url, headers=headers)
        print(resp.status_code)


