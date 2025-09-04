import pandas as pd
import time

def run_etl(input_path, output_path):
    start = time.time()
    df = pd.read_csv(input_path)

    # Transform: drop rows missing 'age' or 'salary'
    df_clean = df.dropna(subset=['age', 'salary'])

    # Add new column: salary band
    df_clean['salary_band'] = df_clean['salary'].apply(
        lambda x: 'high' if x >= 90000 else 'mid'
    )

    df_clean.to_csv(output_path, index=False)
    duration = time.time() - start
    print(f"ETL completed in {duration:.2f} seconds.")
    return df_clean, duration

if __name__ == '__main__':
    input_file = 'data/sample_data.csv'
    output_file = 'reports/cleaned_data.csv'
    df_out, elapsed = run_etl(input_file, output_file)
