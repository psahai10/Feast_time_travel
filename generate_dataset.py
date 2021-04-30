import time
from feast import FeatureStore, ValueType
import pandas as pd
from datetime import datetime

store = FeatureStore(repo_path="feast_repo")

startTime = time.time()
entity_df = pd.DataFrame.from_dict({
    "user_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "event_timestamp": [
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
        datetime(2021, 4, 21, 17, 58, 9),
    ]
})
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:daily_transactions',
        'driver_hourly_stats:total_transactions',
    ],
).to_df()
print(training_df)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

startTime = time.time()
entity_df = pd.DataFrame.from_dict({
    "user_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "event_timestamp": [
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
        datetime(2021, 4, 24, 17, 58, 9),
    ]
})
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:daily_transactions',
        'driver_hourly_stats:total_transactions',
    ],
).to_df()
print(training_df)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

startTime = time.time()
entity_df = pd.DataFrame.from_dict({
    "user_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "event_timestamp": [
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
        datetime(2021, 4, 27, 17, 58, 9),
    ]
})
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:daily_transactions',
        'driver_hourly_stats:total_transactions',
    ],
).to_df()
print(training_df)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))


startTime = time.time()
entity_df = pd.DataFrame.from_dict({
    "user_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "event_timestamp": [
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
        datetime(2021, 4, 30, 17, 58, 9),
    ]
})
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:daily_transactions',
        'driver_hourly_stats:total_transactions',
    ],
).to_df()
print(training_df)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
