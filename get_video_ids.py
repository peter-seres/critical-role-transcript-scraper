import dotenv
import os
import googleapiclient.discovery
from typing import List


def get_video_ids(playlist_id: str) -> List[str]:
    """

    This function makes a request to the youtube API to get the video id of each video in a playlist.
    https://developers.google.com/youtube/v3/docs/playlistItems/list

    """

    # Load .env file for API_KEY.
    dotenv.load_dotenv()
    API_KEY = os.getenv('API_KEY')

    # Build a connected client
    youtube_client = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

    # Make a request (note, only the 'snippet' part has been requested)
    request = youtube_client.playlistItems().list(part=['snippet'], playlistId=playlist_id, maxResults=150)
    response = request.execute()

    # Parse the response for video ids.
    v = response['items']
    video_ids = [pli['snippet']['resourceId']['videoId'] for pli in v if pli['snippet']['resourceId']['kind'] ==
                 'youtube#video']

    print(f"Log: fetched a list of ids with length {len(video_ids)}")

    return video_ids


if __name__ == "__main__":
    from file_utils import write_list_to_file

    # The target playlist:
    playlist_c2 = "PL1tiwbzkOjQxD0jjAE7PsWoaCrs0EkBH2"
    playlist_c2_56_106 = "PLSfHqeFi5OyZRkEH5dQx2LiQLzJK5CcGr"
    playlist_c2_107_129 = "PLSfHqeFi5OybrWfocG0tnyAbiDp04xRib"

    l_1 = get_video_ids(playlist_id=playlist_c2_56_106)
    l_2 = get_video_ids(playlist_id=playlist_c2_107_129)

    write_list_to_file(l_1, "c2_56_106.txt")
    write_list_to_file(l_2, "c2_107_129.txt")
