import os
import pathlib 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s: ')

project_name = "youtube-data-pipeline"

list_of_files = [
    # Main directories with __init__.py files
    f"{project_name}/dags/__init__.py",
    f"{project_name}/scripts/__init__.py",
    f"{project_name}/research/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/raw/.gitkeep",
    f"{project_name}/data/processed/.gitkeep",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/logs/.gitkeep",
    
    # Main files
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",
    f"{project_name}/.gitignore",
    
    # Configuration files
    f"{project_name}/config/config.py",
    
    # Research notebooks
    f"{project_name}/research/api_exploration.ipynb",
    f"{project_name}/research/data_analysis.ipynb",
    
    # Script files
    f"{project_name}/scripts/extract_youtube_data.py",
    f"{project_name}/scripts/transform_data.py",
    f"{project_name}/scripts/load_data.py",
    
    # Airflow DAG
    f"{project_name}/dags/youtube_etl_dag.py",
    
    # Test files
    f"{project_name}/tests/test_scripts.py",
]

# Create the main project directory
os.makedirs(project_name, exist_ok=True)
logging.info(f"Creating main project directory: {project_name}")

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

print(f"\n✅ Project structure for '{project_name}' created successfully!")
print(f"📁 Navigate to ./{project_name} to start working on your project")