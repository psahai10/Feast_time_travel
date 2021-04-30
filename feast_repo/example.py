# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
driver_hourly_stats = FileSource(
    path="/Users/PSahai/Documents/DataScience/Feast_demo/demo_nike/time_travel/feast_repo/data/dummy_data_drivers.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
driver = Entity(name="user_id", value_type=ValueType.INT64, description="user id",)

# Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    entities=["user_id"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="daily_transactions", dtype=ValueType.FLOAT),
        Feature(name="total_transactions", dtype=ValueType.FLOAT),
        # Feature(name="avg_daily_trips", dtype=ValueType.INT64),
    ],
    online=True,
    input=driver_hourly_stats,
    tags={},
)
