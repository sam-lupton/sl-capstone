from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
from tqdm import tqdm_notebook
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'API--key--here'
client_secret = 'API--secret--here'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

def artist_tracks(artists):
    
    '''
    Takes a list of artist names, iterates through their Spotify albums, checks for 
    duplicate albums, then appends all the tracks in those albums to a list of lists
    '''
    
    trax = []
    
    
    
    for artist in tqdm_notebook(artists):
    
        artist_uri = sp.search(artist)['tracks']['items'][0]['artists'][0]['uri']

        # New list of the artist's albums for checking
        albumz = []
        
        

        for i, album in enumerate(sp.artist_albums(artist_uri, album_type='album', limit=None)['items']):

            # Add the artist names and the album names for the album in question to the checklist
            album_check = [j['name'] for j in sp.artist_albums(artist_uri, album_type='album', limit=None)['items'][i]['artists']]
            album_check.append(sp.artist_albums(artist_uri, album_type='album', limit=None)['items'][i]['name'])

            # Only continue scraping if the specific artist and album isn't in the checklist
            if album_check not in albumz:
                albumz.append(album_check)

                trax.extend([[artist, album['name'], album['uri'], song['name'],

                  album['release_date']] + list(sp.audio_features(song['uri'])[0].values()) 
                               for song in sp.album_tracks(album['uri'])['items']])
                
    return trax