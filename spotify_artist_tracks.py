from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
from tqdm import tqdm_notebook
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '5cf34aa394ce41348e14e191abcbcabf'
client_secret = '0614e00064074071a42582fc6acda813'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

def artist_all_tracks(artists):
    
    '''
    Takes a list of artist names, iterates through their Spotify albums (including
    singles, compilations and collaborations), checks for duplicate albums, then
    appends all the tracks in those albums to a list of lists
    '''
    
    # Each list in this list will be a track and its features
    tracks = []
    
    
    
    for artist in tqdm_notebook(artists):
        
        # Get the artist URI (a unique ID)
        artist_uri = sp.search(artist)['tracks']['items'][0]['artists'][0]['uri']

        # Spotify has a lot of duplicate albums, but we'll cross-reference them with this list to avoid extra loops
        album_checker = []
        
        # The starting point of our loop of albums for those artists with more than 50
        n = 0
        
        # Note that here we include singles, compilations and collaborations in the albums to loop through
        while len(sp.artist_albums(artist_uri, limit=50, offset = n)['items']) > 0:
            
            # Avoid overloading Spotify with requests by assigning the list of album dictionaries to a variable
            dict_list = sp.artist_albums(artist_uri, limit=50, offset = n)['items']
            
            for i, album in tqdm_notebook(enumerate(dict_list)):

                # Add the featured artists for the album in question to the checklist
                check_this_album = [j['name'] for j in dict_list[i]['artists']]
                # And the album name
                check_this_album.append(dict_list[i]['name'])
                # And its date
                check_this_album.append(dict_list[i]['release_date'])

                # Only continue looping if that album isn't in the checklist
                if check_this_album not in album_checker:
                    
                    # Add this album to the checker
                    album_checker.append(check_this_album)
                    # For every song on the album, get its descriptors and features in a list and add to the tracklist
                    tracks.extend([[artist, album['name'], album['uri'], song['name'],

                      album['release_date']] + list(sp.audio_features(song['uri'])[0].values()) 
                                   for song in sp.album_tracks(album['uri'])['items']])
            
            # Go through the next 50 albums (otherwise we'll get an infinite while loop)
            n += 50

    return tracks

def artist_tracks(artists):
    
    '''
    Takes a list of artist names, iterates through their Spotify albums, checks for 
    duplicate albums, then appends all the tracks in those albums to a list of lists
    '''
    
    # Each list in this list will be a track and its features
    tracks = []
    
    
    
    for artist in tqdm_notebook(artists):
        
        # Get the artist URI (a unique ID)
        artist_uri = sp.search(artist)['tracks']['items'][0]['artists'][0]['uri']

        # Spotify has a lot of duplicate albums, but we'll cross-reference them with this list to avoid extra loops
        album_checker = []
        
        # The starting point of our loop of albums for those artists with more than 50
        n = 0
        
        # Note the album_type = 'album'. This discounts singles, compilations and collaborations
        while len(sp.artist_albums(artist_uri, album_type = 'album', limit=50, offset = n)['items']) > 0:
            
            # Avoid overloading Spotify with requests by assigning the list of album dictionaries to a variable
            dict_list = sp.artist_albums(artist_uri, album_type = 'album', limit=50, offset = n)['items']
            
            for i, album in tqdm_notebook(enumerate(dict_list)):

                # Add the featured artists for the album in question to the checklist
                check_this_album = [j['name'] for j in dict_list[i]['artists']]
                # And the album name
                check_this_album.append(dict_list[i]['name'])
                # And its date
                check_this_album.append(dict_list[i]['release_date'])

                # Only continue looping if that album isn't in the checklist
                if check_this_album not in album_checker:
                    
                    # Add this album to the checker
                    album_checker.append(check_this_album)
                    # For every song on the album, get its descriptors and features in a list and add to the tracklist
                    tracks.extend([[artist, album['name'], album['uri'], song['name'],

                      album['release_date']] + list(sp.audio_features(song['uri'])[0].values()) 
                                   for song in sp.album_tracks(album['uri'])['items']])
            
            # Go through the next 50 albums (otherwise we'll get an infinite while loop)
            n += 50

    return tracks