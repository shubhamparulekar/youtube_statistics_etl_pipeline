import os
import sys
from datetime import datetime


from scripts.extract_youtube_data import extract_data, save_data as save_extracted
from scripts.transform_data import load_data as load_raw, transform_data, save_data as save_transformed
from scripts.load_data import load_data as load_processed, save_data as save_final, display_summary



def run_etl_pipeline(query="python", max_results=100):
    print("<-----------------------------------Youtube Data ETL Pipeline ------------------------------------->")
    scripts_dir = os.path.join(os.path.dirname(__file__),'scripts')
    sys.path.append(scripts_dir)

    print("\n1. Running Data Extraction")
    raw_data = extract_data(query, max_results)
    timestamp= datetime.now().strftime('%Y%m%d_%H%M%S')
    raw_filename = f"data/raw/youtube_data_{timestamp}.json"
    save_extracted(raw_data,raw_filename)

    print("\n2. Running Data Transformation")
    raw_data=load_raw(raw_filename)
    processed_df=transform_data(raw_data)
    processed_filename = f"data/processed/youtube_data_{timestamp}.csv"
    save_transformed(processed_df,processed_filename)

    print("\n3. Running Data Load")
    final_df=load_processed(processed_filename)
    display_summary(final_df)
    final_filename=f"data/youtube_data_final_{timestamp}.csv"
    save_final(final_df,final_filename)

    print("<----------------------------------- ETL Pipeline Completed------------------------------------->")


if __name__=="__main__":
    run_etl_pipeline()
    # run_etl_pipeline("makeup",100)

