import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import json
from datetime import datetime

def extract_data(query='data science', max_results=10):
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        print("API key not found.")
        return

    youtube = build("youtube", "v3", developerKey=api_key)

    # Search for videos
    search_request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=max_results,
        type="video"
    )
    search_response = search_request.execute()

    video_ids = []

    for item in search_response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_ids.append(item['id']['videoId'])

    video_request = youtube.videos().list(
        id=','.join(video_ids),
        part="snippet,statistics"
    )
    video_response = video_request.execute()

    videos_data = []
    for video in video_response.get('items', []):
        video_info = {
            'video_id': video['id'],
            'title': video['snippet']['title'],
            'description': video['snippet']['description'],
            'published_at': video['snippet']['publishedAt'],
            'channel_id': video['snippet']['channelId'],
            'channel_title': video['snippet']['channelTitle'],
            'views_count': video['statistics'].get('viewCount', 0),
            'likes_count': video['statistics'].get('likeCount', 0),
            'comments_count': video['statistics'].get('commentCount', 0),
            'extracted_at': datetime.now().isoformat()
        }
        videos_data.append(video_info)
    return videos_data

def save_data(data, filename=None):
    if filename is None:
        timestamp= datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"data/raw/youtube_data_{timestamp}.json"

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Data saved to {filename}")
    return filename

if __name__ == "__main__":
    data= extract_data(query='python programming', max_results=10)
    if data:
        save_data(data)
        