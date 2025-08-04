import os
import pandas as pd

def load_data(filepath):
    df=pd.read_csv(filepath)
    return df


def save_data(df, filename=None):
    if filename is None:
        filename = "data/youtube_data_final.csv"
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    df.to_csv(filename, index=False)
    print(f"Final data saved to {filename}")
    return filename

def display_summary(df):
    print("\nData Summary:")
    print(f"Total records: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    if not df.empty:
        print(f"View count range: {df['view_count'].min()} - {df['view_count'].max()}")
        print(f"Top channels: {df['channel_title'].value_counts().head(3).to_dict()}")

if __name__ == "__main__":
    processed_files = [f for f in os.listdir("data/processed") if f.endswith('.csv')]
    if processed_files:
        latest_file = max(processed_files)
        filepath = f"data/processed/{latest_file}"
        
        df = load_data(filepath)
        display_summary(df)
        save_data(df)