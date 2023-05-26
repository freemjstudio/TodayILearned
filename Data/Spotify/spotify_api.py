# Get Data from Spotify 
# Without user authentication 

import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="",
                                                           client_secret=""))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['track']['items']):
    print(idx, track['name'])