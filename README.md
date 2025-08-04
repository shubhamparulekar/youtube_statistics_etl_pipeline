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
git clone https://github.com/shubhamparulekar/youtube_statistics_etl_pipeline/
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

```    
#Initialize Airflow:
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

**Copy DAG to Airflow directory:**

```
cp youtube-data-pipeline/dags/youtube_etl_dag.py airflow_home/dags/
```
   
**Start Airflow:**
```
airflow webserver --port 8080

# In another terminal
airflow scheduler
``` 
 

**Access Airflow UI:**
     * Open http://localhost:8080
     * Login with admin credentials
     * Enable and trigger the youtube_etl_pipeline DAG


## 🔧 Configuration 
* Environment Variables - All configuration is managed through environment variables in the .env file:
```
# YouTube API
YOUTUBE_API_KEY=your_api_key_here

# Default pipeline parameters
DEFAULT_QUERY=data science
DEFAULT_MAX_RESULTS=10

# Airflow settings
AIRFLOW_DAG_SCHEDULE=@daily
AIRFLOW_MAX_ACTIVE_RUNS=1
     
```

* Customizing the Pipeline 
     * Change search query: Modify DEFAULT_QUERY in .env
     * Adjust result count: Modify DEFAULT_MAX_RESULTS in .env
     * Change schedule: Modify AIRFLOW_DAG_SCHEDULE in .env
     * Add new data sources: Extend the extract script
     * Modify transformations: Update transform_data.py
     
## 📊 Data Analysis 
* Open research/data_analysis.ipynb to analyze: 
     * Top performing channels
       <img width="1185" height="590" alt="image" src="https://github.com/user-attachments/assets/86c2724d-e048-45d8-8814-cd71bd98076e" />

     * View vs like correlations
     <img width="846" height="547" alt="image" src="https://github.com/user-attachments/assets/1ce04fd6-f7d3-49cf-b8cc-c549f024a94f" />

     * Content trends over time
     * <img width="842" height="568" alt="image" src="https://github.com/user-attachments/assets/ecacf028-d62b-4756-ac52-86816b71030d" />

     * Engagement metrics
     <img width="1189" height="590" alt="image" src="https://github.com/user-attachments/assets/0c3977ea-8608-40a9-ac19-a2c52545dc51" />

     * And much more!
     

## 📈 Features 
* Current Features 
     * ✅ Automated YouTube data extraction
     * ✅ Data cleaning and transformation
     * ✅ Local file storage (no cloud costs)
     * ✅ Airflow orchestration
     * ✅ Configurable parameters
     * ✅ Comprehensive logging
     * ✅ Unit tests
     * ✅ Data analysis capabilities
          

* Data Points Collected 
     * Video ID and title
     * Channel information
     * View counts
     * Like counts
     * Comment counts
     * Publication dates
     * Video descriptions
     * Extraction timestamps
     

## 🛠️ Technical Stack 

* **Python 3.8+** - Core programming language
* **Apache Airflow 3.0.3** - Workflow orchestration
* **YouTube Data API v3** - Data source
* **Pandas** - Data manipulation
* **Jupyter Notebooks** - Data exploration and analysis
* **JSON/CSV** - Data storage formats
* **dotenv** - Environment management
     
## 📖 Usage Examples 
* **Basic Pipeline Run** 
```
python main.py
````
 
* **Custom Query Run** 
```
 python main.py "python programming" 20
```

 
 
* **Manual Script Execution** 
```
# Extract data
python scripts/extract_youtube_data.py

# Transform data
python scripts/transform_data.py

# Load data
python scripts/load_data.py
```
 
* **Airflow DAG Trigger** 
```
# Via Airflow UI or CLI
airflow dags trigger youtube_etl_pipeline
```

## 📚 Learning Outcomes 

* This project demonstrates skills in: 
     * **REST API Integration** - Working with YouTube Data API
     * **Data Engineering** - ETL pipeline design
     * **Workflow Orchestration** - Apache Airflow
     * **Data Cleaning** - Pandas data manipulation
     * **Software Engineering** - Project structure, testing, logging
     * **Configuration Management** - Environment variables
     * **Data Analysis** - Insights generation


## 🤝 Contributing 
* Fork the repository
* Create a feature branch
* Commit your changes
* Push to the branch
* Open a pull request
     

## 📄 License 
This project is open source and available under the MIT License. 

## 🙏 Acknowledgments 
* YouTube Data API for providing free access to YouTube data
* Apache Airflow community for the excellent orchestration tool
* Python pandas team for data manipulation capabilities
* Qwen3-Coder for providing troubleshooting advice
     


