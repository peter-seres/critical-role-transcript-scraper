from youtube_transcript_api import YouTubeTranscriptApi as ytta
from file_utils import read_video_ids, write_to_json

""" 
This file takes a list of youtube video ids and fetches the transcripts into a dictionary. 
then writes the results to JSON. 

"""

# Read the youtube video IDs
video_ids = read_video_ids("data/video_ids_c2_1-55.txt")

# Load the transcripts:
transcripts = {}
for i, v in enumerate(video_ids):
    print(f"Fetching transcript for video {i}: {v}")
    transcripts[i] = ytta.get_transcript(v)

write_to_json(transcripts, 'data/transcripts_most_recent.json')
