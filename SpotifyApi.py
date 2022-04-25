import requests

spotify_token = ""
song_name = ""
artist = ""
query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
response = requests.get(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(spotify_token)})
response_json = response.json()
print(response_json)