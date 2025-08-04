import pandas as pd
import json
import os
from datetime import datetime

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def transform_data(data):
    df = pd.DataFrame(data)

    df['view_count'] = pd.to_numeric(df['views_count'], errors='coerce')
    df['like_count'] = pd.to_numeric(df['likes_count'], errors='coerce')
    df['comment_count'] = pd.to_numeric(df['comments_count'], errors='coerce')
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['extracted_at'] = pd.to_datetime(df['extracted_at'])
    df['title'] = df['title'].fillna('').astype(str)
    df['description'] = df['description'].fillna('').astype(str)

    df['published_date'] = df['published_at'].dt.date
    df['published_year'] = df['published_at'].dt.year
    df['published_month'] = df['published_at'].dt.month

    final_columns = ['video_id', 
                     'title', 
                     'description', 
                     'channel_title',
                     'view_count', 
                     'like_count', 
                     'comment_count',
                     'published_at', 
                     'published_date',
                     'published_year', 
                     'published_month', 
                     'extracted_at'
    ]
    return df[final_columns]

def save_data(df, filename=None):
    if filename is None:
        timestamp= datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"data/processed/youtube_data_{timestamp}.csv"

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return filename


if __name__ == "__main__":
    raw_files = [f for f in os.listdir('data/raw') if f.endswith('.json')]
    if raw_files:
        latest_file = max(raw_files)
        filepath = f"data/raw/{latest_file}"

        raw_data= load_data(filepath)
        processed_df = transform_data(raw_data)
        save_data(processed_df)