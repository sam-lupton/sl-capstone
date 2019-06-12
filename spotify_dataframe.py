import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '5cf34aa394ce41348e14e191abcbcabf'
client_secret = '0614e00064074071a42582fc6acda813'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

def df_tracks(tracklist):
    
    '''
    Takes the output of artist_tracks (i.e. a list of lists of tracks),
    puts it in a dataframe and formats it.
    '''

    df = pd.DataFrame(tracklist, columns=['artist',
     'album_name',
     'album_uri',
     'track',
     'release_date'] + list(sp.audio_features('7tr2za8SQg2CI8EDgrdtNl')[0].keys()))

    df.rename(columns={'uri':'song_uri'}, inplace=True)

    df.drop_duplicates(subset=['artist', 'track', 'release_date'], inplace=True)

    # Reorder the cols to have identifiers first, predictors last
    cols = ['artist', 'album_name', 'album_uri', 'track', 'release_date', 'id', 'song_uri', 'track_href',
     'analysis_url', 'type', 'danceability', 'energy', 'key',  'loudness', 'mode', 'speechiness',
     'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']

    df = df[cols]
    
    # Extract the decade (take first 3 numbers + 0!)
    df['decade_start'] = df.release_date.apply(lambda x: int(x[:3]+'0'))
    
    return df