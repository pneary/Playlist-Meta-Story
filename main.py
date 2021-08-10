import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

client_id = '1503a5b603394ab39c408d3d99280437'
client_secret = '3ed8aa250e054b65aacd511394b7ab63'
scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                               redirect_uri=cred.redirect_url, scope=scope))

results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])