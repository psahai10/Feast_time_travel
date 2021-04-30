# Feast_time_travel
Quick overview of Feast time travel
1. Create Feast repository using: feast init -t local feast_repo
2. Get into feast_repo folder: cd feast_repo
3. Initialize local datastorage using: feast apply
4. This will automatically generate a .parquet file in the data folder. Change this parquet file to your own specific one.
This can be easly done in pandas with any csv using df.to_parquet('/my_csv_file.parquet')
5. Change your examples.py files in your feast_repo directory:
    Three main files:
        a) FileSource: directory for your parquet file
        b) Entity: Define a primary key to fetch your features (ie user_id)
        c) FeatureView: The name of your features and their ValueType
6. generate_dataset.py already contains code snippet that can be used to do time_travel to extract create your dataset
based on a previous point in time.
7. Online_predictions.ipynb contains code snippets to use the 'online' feature store to extract the latest value
