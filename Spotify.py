import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN
from requests.structures import CaseInsensitiveDict


# POST
token_response = requests.post(TOKEN_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
token_response_data = token_response.json()
#print("here", token_response.status_code)
# save the access token
spotify_token = token_response_data['access_token']


song_name = "The Very First Night (Taylor's Version) (From The Vault)"
artist = "Taylor Swift"
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
#print(response_json)
print("ok")
print(songs)




request_body = json.dumps({
            "name": "Test",
            "description": "Python Project test",
            "public": False
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

playlist_id = response_json["id"]

print("playlist id: ", playlist_id)

#request_data = json.dumps(songs)

request_data =  "{'uris': [%s],'position': 0}" %songs

request_data = json.dumps(request_data)

query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

query = url = "https://api.spotify.com/v1/playlists/1DYNEcup7BLjaR9NNuRYEJ/tracks?position=1&uris=spotify%3Atrack%3A36Ect8eIKK3HQIK4sKvvtf"

response = requests.post(
            query,
            headers={
                "Accept" : "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(TOKEN),
                "Content-Length": "0"
            }
        )
response_json = response.json()
print(response_json)

"""
url = "https://api.spotify.com/v1/playlists/1DYNEcup7BLjaR9NNuRYEJ/tracks?position=0&uris=spotify%3Atrack%3A36Ect8eIKK3HQIK4sKvvtf"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer {}".format(TOKEN)
headers["Content-Length"] = "0"


resp = requests.post(url, headers=headers)

print(resp.status_code)
"""
