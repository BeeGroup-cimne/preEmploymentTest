import pandas as pd
from datetime import datetime
import sqlite3

df = pd.read_excel("data_management/data_2019.xls",usecols=['d_ini','d_end','kwh']).dropna()


df['date'] = df.apply(lambda x: pd.date_range(x.d_ini,x.d_end,freq='1D'),axis=1)
df = df.explode('date').reset_index(drop=True)
df['kwh/day'] = df.groupby(['d_ini', 'd_end'])['kwh'].transform(lambda x: x.mean() / len(x))

idx = pd.date_range(start=df.date.min(),end=df.date.max())

ts = df.set_index('date').drop(columns=['d_ini','d_end','kwh'])
ts = ts.reindex(idx)
