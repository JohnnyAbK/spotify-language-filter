import requests
from bs4 import BeautifulSoup
import os
from langdetect import detect
import re
import concurrent.futures

GENIUS_CLIENT_ID = 'x'
GENIUS_CLIENT_SECRET = 'x'
GENIUS_CLIENT_ACCESS_TOKEN = 'x'
GENIUS_API_SEARCH_URL = 'https://api.genius.com/search'
GENIUS_BASE_URL = 'https://genius.com'
PLAYLIST_URL = "x"
SPOTIFY_ACCESS_TOKEN = 'x'

def search_song(song_title, song_artist):
    headers = {'Authorization': f'Bearer {GENIUS_CLIENT_ACCESS_TOKEN}'}
    query = f'{song_title} {song_artist}'
    params = {'q': query}
    
    response = requests.get(GENIUS_API_SEARCH_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        hits = data['response']['hits']
        
        if hits:
            song = hits[0]['result']
            song_url = song['url']
            return song_url

        else:
            #print("No songs found.")
            return None
    else:
        print(f"Error searching for song: {response.status_code}")
        return None

def get_lyrics_from_url(song_url):
    response = requests.get(song_url)
    
    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            lyrics_div = soup.find('div', class_='Lyrics-sc-37019ee2-1 jRTEBZ')
            
            if lyrics_div:
                lyrics = lyrics_div.get_text().strip()
                lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
                lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])

                return lyrics
            else:
                #print("Lyrics not found on Genius page.")
                return None
    else:
        print(f"Error retrieving song page: {response.status_code}")
        return None

def detect_language_from_lyrics(lyrics):
    try:
        return detect(lyrics)

    except:
        return None

def extract_playlist_id(url):
    match = re.search(r'playlist/([a-zA-Z0-9]+)', url)

    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid playlist URL")

PLAYLIST_ID = extract_playlist_id(PLAYLIST_URL)
SPOTIFY_API_URL = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/tracks'

def fetch_all_tracks(api_url):
    headers = {
        'Authorization': f'Bearer {SPOTIFY_ACCESS_TOKEN}'
    }
    all_tracks = []
    song_details = []
    while api_url:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_tracks.extend(data['items'])
            api_url = data['next']
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break

    for item in all_tracks:
        track = item['track']
        song_name = track['name']
        artist_name = track['artists'][0]['name']
        song_details.append((song_name, artist_name))
    
    return song_details

def process_song(song_name, artist_name):
    song_url = search_song(song_name, artist_name)
    if not song_url:
        return None, None, None
    
    lyrics = get_lyrics_from_url(song_url)
    if not lyrics:
        return None, None, None
    
    language = detect_language_from_lyrics(lyrics)
    return song_name, artist_name, language

song_details = fetch_all_tracks(SPOTIFY_API_URL)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(lambda song: process_song(song[0], song[1]), song_details)

for song_name, artist_name, lan in results:
    if song_name and artist_name and lan == 'it':
        print(f"{song_name} by {artist_name}", search_song(song_name, artist_name))