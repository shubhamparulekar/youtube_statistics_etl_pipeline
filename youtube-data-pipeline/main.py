import os
import sys
from datetime import datetime
import json


from scripts.extract_youtube_data import extract_data, save_to_json
raw_data=extract_data(query='data science', max_results=20)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

raw_filename = f"../data/raw/youtube_data_{timestamp}.json"
save_to_json(raw_data, raw_filename)