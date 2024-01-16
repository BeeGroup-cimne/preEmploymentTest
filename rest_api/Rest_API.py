import pandas as pd
import mysql.connector
from flask import Flask, request, jsonify
import numpy as np
import os

app = Flask(__name__)

# Create MySQL database
def create_db(database_name):
    try:
        file = open("pwd.txt", 'r')
        pwdd = file.read()
        conn = mysql.connector.connect(
            host='db',
            port=3306,
            user='root',
            password=pwdd.strip()
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully!", flush=True)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}", flush=True)
        return None

# Connect to the MySQL database
def create_table(conn, table_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                kwh FLOAT NuLL
            )
        """)
        print(f"Table '{table_name}' created successfully!", flush=True)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}", flush=True)



# Function to insert data into the daily_time_series table
def insert_data(df, conn, table_name):
    df['kwh'] = df['kwh'].replace({np.nan: None})
    cursor = conn.cursor()
    for index, row in df.iterrows():
        sql = f'''
        INSERT IGNORE INTO {table_name} (id, date, kwh)
        VALUES (%s, %s, %s)
        '''
        values = (index + 1, row['date'], row['kwh'])
        cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Data inserted", flush=True)

def connect_to_db(database):
    try:
        file = open("pwd.txt", 'r')
        pwdd = file.read()
        conn = mysql.connector.connect(
            host='db',
            port=3306,
            user='root',
            password=pwdd.strip(), 
            database=database 
        )
        print("Connected to MySQL!", flush=True)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}", flush=True)
        return None
        

table_name = 'daily_time_series'
database_name = 'daily_time_series_db'
df = pd.read_csv("time_series_daily.csv")
# Flask route to create database, table, and insert data
@app.route('/', methods=['GET'])
def initialize_database():

    with app.app_context():
        create_db(database_name)
        conn = connect_to_db(database_name)
        create_table(conn, table_name)
        insert_data(df, conn, table_name)

    return jsonify({'message': 'Database initialization complete'})

@app.route('/get_data', methods=['GET'])
def get_timeseries():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        # Both start_date and end_date are provided, query for date range
        conn = connect_to_db(database_name)
        cursor = conn.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM {table_name} WHERE date BETWEEN '{start_date}' AND '{end_date}'")
        result = cursor.fetchall()

        if not result:
            return jsonify({'error': 'No data found for the given date range'}), 404

    elif start_date:
        # Only start_date is provided, query for that specific date
        conn = connect_to_db(database_name)
        cursor = conn.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM {table_name} WHERE date = '{start_date}'")
        result = cursor.fetchall()

        if not result:
            return jsonify({'error': 'No data found for the given date'}), 404

    else:
        # Neither start_date nor end_date is provided
        return jsonify({'error': 'At least one of start_date or end_date is required'}), 400

    data = [{"date": row['date'].strftime('%Y-%m-%d'), "kwh": row['kwh']} for row in result]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
    