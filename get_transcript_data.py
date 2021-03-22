from youtube_transcript_api import YouTubeTranscriptApi as ytta
from file_utils import read_video_ids, write_to_json
import time

""" 
This file takes a list of youtube video ids and fetches the transcripts into a dictionary. 
then writes the results to JSON. 

"""

# Read the youtube video IDs
video_ids = read_video_ids("data/video_ids_c2.txt")

# Load the transcripts:
transcripts = {}
for i, v in enumerate(video_ids):
    trial_count = 0
    while trial_count < 5:
        print(f"Fetching transcript for episode {i+1}: {v}, attempt: {trial_count+1}")
        try:
            transcripts[i+1] = ytta.get_transcript(v)
            break
        except Exception as e:
            trial_count += 1
            print(f"error", {e})
            time.sleep(1)

write_to_json(transcripts, 'data/transcripts_most_recent.json')
