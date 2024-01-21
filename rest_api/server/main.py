from fastapi import FastAPI
from starlette.responses import RedirectResponse
from influxdb_client import InfluxDBClient


bucket = "mybucket"
org = "myorg"
url = "http://influxdb:8086"
token = "exampletoken"

client = InfluxDBClient(
    url=url,
    token=token,
    org=org,
)

query_api = client.query_api()
app = FastAPI(
    title= "BeeGroup - PRE-EMPLOYMENT TEST"
)

@app.get("/")
def documentation():
    return RedirectResponse(url="/docs/")
    

@app.get("/data/{start_date}/{end_date}", description= "Get Data by dates: [yyyy-mm-dd / yyyy-mm-dd)")
def get_by_dates(start_date: str, end_date: str):

    query = f"""from(bucket: "{bucket}")\
  |> range(start: {start_date}, stop: {end_date})\
  |> map(fn: (r) => ({{_time: r._time, _value: r._value}}))\
    """
    result = query_api.query(org=org, query=query)

    data = {}
    for table in result:
        for record in table.records:
           data[record.get_time()] =  record.get_value()
    return data