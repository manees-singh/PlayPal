# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:13:49 2023

@author: Ansuman Sharma
"""

import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json

from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/process_data', method=['POST', 'GET'])

def index():
    if request.method=='POST':
        artist_name=request.form['Artist']
        year=request.form['Year']

#This loads environment variable files for us

#load_dotenv()
# create a SpotifyOAuth object with your client ID, client secret, and redirect URI
# auth_manager = SpotifyOAuth(client_id='f6635de84ba24b4cb25638b9d6095c3d',
#                             client_secret='94936c10c5424335acfe9a72f52d961a',
#                             redirect_uri='http://google.com/',
#                             scope='')

# # create a Spotify object with the authenticated access token
# spotify = spotipy.Spotify(auth_manager=auth_manager)

        client_id = 'f6635de84ba24b4cb25638b9d6095c3d'                #enter the client ID from the Settings menu in Spotify
        client_secret = '94936c10c5424335acfe9a72f52d961a'        #enter the client secret from the Settings menu in Spotify

        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


        access_token=client_credentials_manager.get_access_token()
        print(access_token)
        spotify=spotipy.Spotify(auth=access_token['access_token'])
                        #Use the search method to search for the artist by name, and retrieve their id.
        #---------------REMEMBER TO SET THE ARTIST NAME TO WHATEVER THE USER ENTERS ON THE WEBPAGE-----------------
        result = sp.search(artist_name, limit=1, type="artist")
        artist_id = result['artists']['items'][0]['id']
        albums = sp.artist_albums(artist_id, album_type="album")    #Use the artist_albums method to retrieve a list of all albums by the artist
        #The code below prints 10 songs of the specified artist
        def same_artist_list(artist_name = None):
            if artist_name is not None:
                tracks = []
                track_names = []
                name_of_artist = artist_name
                results = spotify.search(q='artist:' + artist_name, type='track', limit = 10)
                tracks = results['tracks']['items']
                for track in tracks:
                    track_names.append(track['name']+' ('+track['album']['release date'].split('-')[0]+')')
                if len(track_names) < 10:
                    track_names.append("We're sorry, we couldn't ")
                return track_names
            else:
                return None

        #the code below returns the song names along with the year of publication
        def same_year_list(artist_name = None):
            if artist_name is not None:
                track_names = []
                name_of_artist = artist_name
                year = (input("Enter the year of release: "))
                search_offset = 0
                results = spotify.search(q='artist:' + name_of_artist, type='track', limit = 50, offset = search_offset)
                tracks = results['tracks']['items']

        # Loop through the pages of results
                while len(tracks) < 151:
                    search_offset += 50  # Increment the offset to retrieve the next page
                    results = spotify.search(q='artist:' + name_of_artist, type='track', limit=50, offset=search_offset)
                    tracks += results['tracks']['items']

                for track in tracks:
                    if (track['album']['release_date'].split('-')[0]) == year:
                        if track['name'] not in track_names:
                            track_names.append(track['name']+' ('+track['album']['release date'].split('-')[0]+')')
                        if len(track_names) >= 10:
                            break
                    if len(track_names) >= 10:
                        break
                    #for track in tracks:
                    #   track_names.append(track['name'])
                return track_names
            else:
                track_names = []
                year = (input("Enter the year of release: "))
                search_offset = 0
                results = spotify.search(q='artist:' + name_of_artist, type='track', limit = 50, offset = search_offset)
                tracks = results['tracks']['items']
                for track in tracks:
                    if (track['album']['release_date'].split('-')[0]) == year:
                        if track['name'] not in track_names:
                            track_names.append(track['name'])

                        if len(track_names) >= 10:
                            break
                    if len(track_names) >= 10:
                        break
                return track_names
        '''
        def same_genre_list(artist_name = None, year = None):
            if artist_name == None:
                tracks = []
                for album in albums['items']:
                    # Get the full album details
                    album_details = sp.album(album['id'])
                    # Extract the album genres
                    genres = album_details['genres']
                    # Get the first genre in the list (if any)
                    genre = genres[0] if len(genres) > 0 else ""
                    album_tracks = sp.album_tracks(album['id'], limit=10)
                    for track in album_tracks['items']:
                        # Get the full track details
                        track_details = sp.track(track['id'])
                        # Extract the year of publication from the release date
                        release_date = track_details['album']['release_date']
                        year = release_date.split('-')[0]
                        # Append the track details, year, and genre to the list
                        tracks.append({'name': track_details['name'], 'album': track_details['album']['name'], 'year': year, 'genre': genre})
                        if len(tracks) >= 10:
                            break
                    if len(tracks) >= 10:
                        break

        # Print the list of tracks with their year of publication and genre
                for track in tracks:
                    print(track['name'], "-", track['album'], "-", track['year'], "-", track['genre'])

            
        '''
