# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Billboard Top 100 + Genre Artists dataset

Path: 'clean.csv'

This dataset stems from scraping a list of artists from the [Billboard Top 100 Artists of All Time](https://www.billboard.com/charts/greatest-hot-100-artists), supplemented with the [top 10 artists](https://www.thetoptens.com/best-blues-artists/) of various genres as scraped from https://www.thetoptens.com/. Having extracted songs by those artists from Spotify, I have removed all compilations, 'best of' albums, greatest hits, remasters, deluxe and anniversary editions, as well as live recordings, leaving only the oldest represented version of each song, to maximise the chance of it being the original.

--------------------

**Data Set Characteristics:**

    :Number of Instances: 25213
    :Number of Attributes: 24 (10 identifying attributes, 13 numeric predictive features, and the decade of release as a target)
    :Attribute Information:

artist				         - The name of the track's artist.

album_name			         - The name of the track's album.

album_uri			         - Album's unique URI.

track				         - The name of the track.

release_date		         - The YYYY-MM-DD date of the album's release.

id				             - The track's unique identifier (same as URI but without parameters for type of object).

song_uri			        - The track’s unique URI

track_href			        - A link to the Web API endpoint providing full details of the track.

analysis_url	    	    - An HTTP URL to access the full audio analysis of this track. An access token is required to access this data.

type			    	    - The object type: “audio_features”.

danceability(float)  	    - Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

key(int)                	- The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C#, 2 = D, and so on. If no key was detected, the value is -1.

energy(float)              	- Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

mode(int)                   - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.

key(int)		        	- The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.

loudness(float)             - The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.

mode(int)			        - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.

speechiness(float)		    - Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. 

acousticness(float)         - A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

instrumentalness(float)     - Predicts whether a track contains no vocals. oh and ah sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly vocal. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. 

liveness(float)             - Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. 

valence(float)             	- A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). 

tempo(float)            	- The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.

duration_ms(int)          	- The duration of the track in milliseconds.

time_signature(int)         - An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).

decade_start 			    - The YYYY date of the beginning of the decade from which the album comes.


    :Missing Attribute Values: None
