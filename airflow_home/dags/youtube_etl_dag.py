from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import os
import sys

project_root = '/home/sdp/python/youtube_data_pipeline/youtube-data-pipeline'
scripts_path = os.path.join(project_root, 'scripts')
sys.path.insert(0, project_root)
sys.path.insert(0, scripts_path)

from extract_youtube_data import extract_data, save_data as save_extracted
from transform_data import load_data as load_raw, transform_data, save_data as save_transformed
from load_data import load_data as load_processed, save_data as save_final, display_summary



def extract_youtube_data(**context):
    print("<------------------------------------starting youtube data extraction------------------------------------->")

    # <--------------------------------------change this line for custom queries------------------------------------->
    raw_data = extract_data("python", 10)
    # <-------------------------------------------------------------------------------------------------------------->

    timestamp= datetime.now().strftime('%Y%m%d_%H%M%S')
    raw_filename = f"data/raw/youtube_data_{timestamp}.json"
    save_extracted(raw_data,raw_filename)

    context['task_instance'].xcom_push(key='raw_filename', value=raw_filename)
    print(f"Extracted {len(raw_data)} videos")



def transform_youtube_data(**context):
    print("<-------------------------------------Starting data transformation-------------------------------------->")

    raw_filename = context['task_instance'].xcom_pull(key='raw_filename', task_ids='extract_task')
    
    raw_data = load_raw(raw_filename)
    processed_df = transform_data(raw_data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    processed_filename = f"{project_root}/data/processed/youtube_data_{timestamp}.csv"
    save_transformed(processed_df, processed_filename)

    context['task_instance'].xcom_push(key='processed_filename', value=processed_filename)
    print(f"Transformed {len(processed_df)} records")



def load_youtube_data(**context):
    print("<------------------------------------------Starting data loading------------------------------------------>")
          
    processed_filename = context['task_instance'].xcom_pull(key='processed_filename', task_ids='transform_task')
    display_summary(final_df)
    
    final_filename = f"{project_root}/data/youtube_data_final.csv"
    save_final(final_df, final_filename)
    
    print("ETL pipeline completed!")


default_args = {
    'owner': 'youtube-pipeline',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 8),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'youtube_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for YouTube data',
    schedule='@daily',
    catchup=False,
    tags=['youtube', 'etl'],
)

# Create tasks
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_youtube_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_youtube_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_youtube_data,
    dag=dag,
)

# Set task order
extract_task >> transform_task >> load_task