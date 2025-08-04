## YouTube Data Engineering Pipeline 

A complete end-to-end data engineering project that extracts YouTube data, processes it through an ETL pipeline, and orchestrates it with Apache Airflow - all running locally and completely free. 

### 📋 Project Overview 
* Extracts data from YouTube Data API v3
* Transforms and cleans the data
* Loads processed data to local storage
* Orchestrates the entire process with Apache Airflow
* Provides analysis and insights
     

### 🏗️ Project Architecture 
```
YouTube API → Extract → Transform → Load → Airflow Orchestration → Analysis
```

### Data Flow: 
* Extract: Pull video data from YouTube API based on search queries
* Transform: Clean data, convert data types, create derived columns
* Load: Save processed data to CSV files
* Orchestrate: Apache Airflow manages the pipeline execution
* Analyze: Jupyter notebooks provide data insights

### 📁 Project Structure
```
youtube-data-pipeline/
├── config/                     # Configuration files
│   ├── __init__.py
│   └── config.py              # Environment and path configuration
├── scripts/                    # ETL scripts
│   ├── __init__.py
│   ├── extract_youtube_data.py # Extract data from YouTube API
│   ├── transform_data.py       # Clean and transform data
│   └── load_data.py           # Save final processed data
├── dags/                       # Airflow DAG definitions
│   └── youtube_etl_dag.py     # Main ETL pipeline DAG
├── research/                   # Jupyter notebooks for exploration
│   ├── api_exploration.ipynb  # API testing and exploration
│   └── data_analysis.ipynb    # Data analysis and visualization
├── data/                       # Data storage
│   ├── raw/                   # Raw JSON data from API
│   ├── processed/             # Cleaned CSV data
│   └── youtube_data_final.csv # Final consolidated data
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_extract.py        # Tests for extract functionality
│   └── test_transform.py      # Tests for transform functionality
├── airflow_home/              # Airflow installation directory
│   ├── dags/                  # Airflow DAGs (symlink or copy)
│   ├── logs/                  # Airflow logs
│   └── plugins/               # Airflow plugins
├── requirements.txt           # Python dependencies
├── main.py                   # Main pipeline runner
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

### 🚀 Getting Started 
**Prerequisites** 
* Python 3.8+
* Virtual environment (recommended)
* Google Cloud account (free tier)
* YouTube Data API v3 enabled
     

**Installation** 
* Clone the repository:
     
```
git clone <your-repo-url>
cd youtube-data-pipeline
```
 
* Create virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
 
* Install dependencies:
```
pip install -r requirements.txt
```
 
* Set up YouTube API:
     * Go to Google Cloud Console 
     * Create a new project or select an existing one
     * Enable YouTube Data API v3
     * Create API credentials (API Key)
     * Copy your API key
         
* Configure environment variables:
     * Create a .env file in the project root:

  ```
     YOUTUBE_API_KEY=your_actual_api_key_here
     DEFAULT_QUERY=data science
     DEFAULT_MAX_RESULTS=10
     AIRFLOW_DAG_SCHEDULE=@daily
  ```

**Running the Pipeline** 
* Option 1: Manual Execution 
```
# Run the complete ETL pipeline manually
python main.py

# Run with custom parameters
python main.py "machine learning" 15
```

* Option 2: Airflow Orchestration 
     * Initialize Airflow:
```    
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

     * Copy DAG to Airflow directory:
     

bash
 
 
1
cp youtube-data-pipeline/dags/youtube_etl_dag.py airflow_home/dags/

    Start Airflow:
     

bash
 
 
1
2
3
4
5
# In one terminal
airflow webserver --port 8080

# In another terminal
airflow scheduler
 
 

    Access Airflow UI:
        Open http://localhost:8080
        Login with admin credentials
        Enable and trigger the youtube_etl_pipeline DAG
         
     
