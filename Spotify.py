import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN


class Spotify():
    def __init__(self):
        self.token_url = "https://accounts.spotify.com/api/token"

    def __get_token(self):
        token_response = requests.post(self.token_url, {
                                                'grant_type': 'client_credentials',
                                                'client_id': CLIENT_ID,
                                                'client_secret': CLIENT_SECRET,
                                                })

        # convert the response to JSON
        token_response_data = token_response.json()
        print("here", auth_response.status_code)
        # save the access token
        spotify_token = token_response_data['access_token']
        return spotify_token

    def query_song(self, song_name, artist):
        spotify_token = self.__get_token()
        song_name = "The Very First Night (Taylor's Version) (From The Vault)"
        artist = "Taylor Swift"
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                    song_name,
                    artist
                )
        response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        print(response_json)

    def check_response(self, response):
        # check for valid response status
        if response.status_code != 200:
            raise ResponseException(response.status_code)







# POST
token_response = requests.post(TOKEN_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
token_response_data = token_response.json()
print("here", token_response.status_code)
# save the access token
spotify_token = token_response_data['access_token']

song_name = "The Very First Night (Taylor's Version) (From The Vault)"
artist = "Taylor Swift"
song_name = "wrap"
artist = "Cardi B"
query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
userID ="yj46x5ujbzvzvwlxfidiwxwt8"
#userID = "me"
query2 = "https://api.spotify.com/v1/users/{user_id}".format(user_id=userID)
response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
response_json = response.json()
songs = response_json["tracks"]["items"][0]["uri"]
print(response_json)
print("ok")
print(songs)

"""
test auth code
"""
user_authorization_code = requests.get(
        AUTH_URL, {
            'client_id': CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': SPOTIFY_REDIRECT_URI,
            'scope':  SCOPE2,
        }
    )

print(user_authorization_code)



"""Create A New Playlist"""

request_body = json.dumps({
            "name": "Test",
            "description": "Python Project test",
            "public": True
        })

print("test")
query = "https://api.spotify.com/v1/users/{}/playlists".format(userID)

response = requests.post(
            query,
            data=request_body,
            headers={
                "Accept" : "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(TOKEN)
            }
        )
response_json = response.json()

#playlist_id = response_json["id"]

#print("playlist id: ", playlist_id)
"""
request_data = json.dumps(songs)

request_data =  "{'uris': [%s],'position': 0}" %songs

request_data = json.dumps(request_data)

query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(TOKEN)
            }
        )
response_json = response.json()
print(response_json)


"""