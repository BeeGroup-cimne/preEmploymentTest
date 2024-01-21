from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import time

bucket = "mybucket"
org = "myorg"
url = "http://influxdb:8086"
token = "exampletoken"

client = InfluxDBClient(
    url=url,
    token=token,
    org=org,
)

write_api = client.write_api(write_options=SYNCHRONOUS)

def load_data():
    csv_file = "./timeseries_BeeGroup.csv"
    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():
        p = Point("Consumption").field("kwh",row["kwh"]).time(row["date"])
        print(p, flush=True)
        try:
            write_api.write(bucket=bucket,org=org, record=p)
        except Exception as e:
            print(f"Error writing data to InfluxDB: {e}")

    print("Data loaded successfully", flush=True)

if __name__ == '__main__':
    time.sleep(5)
    print("Loading data...", flush= True)
    load_data()
