import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN
from requests.structures import CaseInsensitiveDict

class Spotify2():
    def __init__(self):
        self.token_url = TOKEN_URL
        self.artist = "Taylor Swift"
        self.userID = "yj46x5ujbzvzvwlxfidiwxwt8"
        self.songs_name = ["The Other Side Of The Door (Taylor's Version)", "Tell Me Why (Taylor's Version)","The Last Time (feat. Gary Lightbody of Snow Patrol) (Taylor's Version)"]

    def __get_token(self):
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
    
    def get_song_uri(self):
        spotify_token = self.__get_token()
        song_name = "The Very First Night (Taylor's Version) (From The Vault)"
        song_name2 = self.songs_name[0]
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                    song_name,
                    self.artist
                )
        response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        print(response_jsonstatus_code)
        if response_json.status_code == 200 :
            song_uri = response_json["tracks"]["items"][0]["uri"]
            return song_uri
        
    def get_user_id(self):
        url = "https://api.spotify.com/v1/me"
        #spotify_token = self.__get_token()
        spotify_auth = "BQBuMz-olPOz2JiFtK-91pWLWwIoDdaA_69WlMaEBehKEMfk794-KkiHONhhJ4ygYJ1vYg9OwRLZtWcb33yaObUTZGEhbJIwwAGjGyXGtMNdhVEA0vAgQuJqeAA7-NjiAZg1-k_-KP3VpSnhh8L7w0kBtomOTSKQXSwbwTuzZVyYVa3UEZorffv19RkiWMS81UvSbLr2pb-eYU7mHPvA9qgi4RgkxQ2Hl0FQ0lCb7DyxWg"
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
  
    def get_song_uri2(self, song_name):
        spotify_token = self.__get_token()
        spotify_token = ""
        #spotify_auth =  self.__get_auth()
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=1".format(
                    song_name,
                    self.artist
                )
        response = requests.get(query,headers={"Content-Type": "application/json",
                                               "Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        print(response_json)
        if response_json.code == 200:
            song_uri = response_json["tracks"]["items"][0]["uri"]
            return song_uri
        

a = Spotify2().get_user_id()
