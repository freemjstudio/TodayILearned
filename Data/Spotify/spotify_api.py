# Get Data from Spotify 
# Without user authentication 
from test import * 

import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='Oasis', limit=20)
for idx, track in enumerate(results['track']['items']):
    print(idx, track['name'])