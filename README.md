# Critical Role Transcripts

This repo contains code that can fetch youtube transcripts from the Critical Role's video content.
The data then can be used for any fun NLP experimentation.

## Files

* **get_video_ids.py**: uses google api to fetch the video id of each video in a playlist. Only works for max 50 elements 
for some reason.

* **get_transcript_data.py**: downloads the transcripts from a list of youtube video ids (last part of the url) 
and saves them to a JSON file.

* **file_utils.py**: saving data to files and loading data from files.

* **read_transcripts.py: ** reads the json data and finds speaker and dialogue text units. Filters out players and dms.

## todos

* NLP experimentation

## Resources

https://github.com/roddds/critrole/blob/master/criticalrole%20talking.ipynb
