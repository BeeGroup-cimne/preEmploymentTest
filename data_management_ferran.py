import pandas as pd
import numpy as np

def transform(file_name):
    """
    Transform the input data from an Excel file into a time series with regular daily frequency.
    Save the resulting time series as a CSV file.

    Parameters:
    - file_name (str): The name of the Excel file containing the input data.
    """
    # Read data from Excel file into a DataFrame
    df = pd.read_excel(file_name)
    
    # Extract only the first three columns
    df = df.iloc[:, :3] 

    # Drop rows with NaN values
    df = df.dropna()

    # Convert date columns to datetime format
    df['d_ini'] = pd.to_datetime(df['d_ini'])
    df['d_end'] = pd.to_datetime(df['d_end'])

    # Set the desired start date (if you want full year)
    start_date = pd.to_datetime('2019-01-01')

    # Initialize an empty DataFrame for the expanded time series
    expanded_df = pd.DataFrame(columns=['date', 'kwh'])

    # Create a DataFrame with all dates in daily frequency
    final_csv = pd.date_range(start=start_date, # If you want the first date to be the first date of the given csv, you have to do the following: start=df['d_ini'].min()
                              end=df['d_end'].max(),
                              freq='D')
    final_csv = pd.DataFrame({'date': final_csv})

    # Iterate over rows in the original DataFrame and expand the time series
    for _, row in df.iterrows():
        date_range = pd.date_range(start=row['d_ini'],
                                   end=row['d_end'],
                                   freq='D')
        row_df = pd.DataFrame({"date": date_range, "kwh": row['kwh']})
        expanded_df = pd.concat([expanded_df, row_df])

    # Reset the index of the expanded DataFrame
    expanded_df = expanded_df.reset_index(drop=True)

    # Merge the final time series DataFrame with the expanded DataFrame
    final_csv = pd.merge(final_csv, expanded_df, how='left')

    # Replace NaN values with the string "NaN" in the 'kwh' column
    final_csv['kwh'] = np.where(final_csv['kwh'].isnull(), "NaN", final_csv['kwh'])

    # Save the final time series as a CSV file
    final_csv.to_csv("time_series_daily.csv", index=False)

if __name__ == '__main__':
    file_name = "data_management/data_2019.xls"
    transform(file_name)
