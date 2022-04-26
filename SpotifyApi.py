import requests
from config import CLIENT_ID, CLIENT_SECRET, AUTH_URL 


class Spotify():
    def __init__(self):
        self.auth_url = "https://accounts.spotify.com/api/token"

    def __get_token(self):
        auth_response = requests.post(self.auth_url, {
                                                'grant_type': 'client_credentials',
                                                'client_id': CLIENT_ID,
                                                'client_secret': CLIENT_SECRET,
                                                })

        # convert the response to JSON
        auth_response_data = auth_response.json()
        # save the access token
        spotify_token = auth_response_data['access_token']
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
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
spotify_token = auth_response_data['access_token']

song_name = "The Very First Night (Taylor's Version) (From The Vault)"
artist = "Taylor Swift"
song_name = "wrap"
artist = "Cardi B"
query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
response_json = response.json()
songs = response_json["tracks"]["items"][0]["uri"]
print(songs)

