from fastapi import FastAPI, Query, Depends, HTTPException
import duckdb
import json

app = FastAPI()
db = duckdb.connect(database='electricity.db', read_only=True)


def validate_groupby_aggr(groupby: str = Query(None, description="year / month"),
                           aggr: str = Query(None, description="avg / sum / min / max")):
    if groupby and not aggr:
        raise HTTPException(status_code=400, detail="If groupby is provided, aggr must also be provided.")
    if not groupby and aggr:
        raise HTTPException(status_code=400, detail="If aggr is provided, groupby must also be provided.")
    return groupby, aggr


@app.get('/consumption')
async def read_item(
    start_date: str = Query(None, description="yyyy-mm-dd"),
    end_date: str = Query(None, description="yyyy-mm-dd"),
    groupby_aggr: tuple = Depends(validate_groupby_aggr)
):
    
    if groupby_aggr[0] and groupby_aggr[1]:
        query = f"SELECT EXTRACT('{groupby_aggr[0]}' FROM date) AS year, {groupby_aggr[1]}(kwh) AS kwh FROM consumption"
    else:
        query = "SELECT * FROM consumption"
    
    if start_date:
        query += f" WHERE date >= '{start_date}'"
    if end_date:
        conjunction = "AND" if start_date else "WHERE"
        query += f" {conjunction} date <= '{end_date}'"
        
    if groupby_aggr[0] and groupby_aggr[1]:
        query += f" GROUP BY EXTRACT('{groupby_aggr[0]}' FROM date)" 
        
    
    df = db.execute(query).fetch_df()
    entries = df.to_json(orient='records', date_format='iso')
    return json.loads(entries)

# if __name__ == '__main__':
#     uvicorn.run(app, host='120.0.0.1', port=8000)