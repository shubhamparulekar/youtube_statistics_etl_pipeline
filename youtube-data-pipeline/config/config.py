import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# YouTube API Configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
DEFAULT_QUERY = os.getenv('DEFAULT_QUERY', 'data science')
DEFAULT_MAX_RESULTS = int(os.getenv('DEFAULT_MAX_RESULTS', '10'))

# File Paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Airflow Configuration
AIRFLOW_DAG_SCHEDULE = os.getenv('AIRFLOW_DAG_SCHEDULE', '@daily')
AIRFLOW_MAX_ACTIVE_RUNS = int(os.getenv('AIRFLOW_MAX_ACTIVE_RUNS', '1'))

# Create directories if they don't exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)