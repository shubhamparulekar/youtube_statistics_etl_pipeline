import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def test_youtube_api():
    load_dotenv()
    api_key=os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        print("YOUTUBE_API_KEY is not set in the environment variables.")
        return False
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.search().list(
            part="snippet",
            q="data science",
            maxResults=5
        )
        response = request.execute()
        print("YouTube API Connection Successful!")
        print(f"Found {len(response['items'])} items")
        
        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                print(f"- {item['snippet']['title']}")
        
        return True
        
    except Exception as e:
        print(f"Error connecting to YouTube API: {e}")
        return False

if __name__ == "__main__":
    test_youtube_api()



# print(f"API Key length: {len(api_key) if api_key else 0}")

# try:
#     youtube = build('youtube', 'v3', developerKey=api_key)

#     request = youtube.channels().list(
#         part='snippet',
#         id='UCBJycsmduvYEL83R_U4JriQ'
#     )
#     response = request.execute()
    
#     print("Success!")
#     print(f"Found {len(response['items'])} channels")
    
# except Exception as e:
#     print(f"Error: {e}")