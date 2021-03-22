import dotenv
import os
import googleapiclient.discovery

""" This file makes a request to the youtube API to get the video id of each video in a playlist. """
""" It's only good for a max number of 50 though..."""
# https://developers.google.com/youtube/v3/docs/playlistItems/list

# The target playlist:
PLAYLIST = "PL1tiwbzkOjQxD0jjAE7PsWoaCrs0EkBH2"

# Load .env file for API_KEY.
dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')

# Build a connected client
youtube_client = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

# Make a request (note, only the 'snippet' part has been requested)
request = youtube_client.playlistItems().list(part=['snippet'], playlistId=PLAYLIST, maxResults=150)
response = request.execute()

# Parse the video ids out of the json:
v = response['items']

video_ids = [pli['snippet']['resourceId']['videoId'] for pli in v if pli['snippet']['resourceId']['kind'] ==
             'youtube#video']
