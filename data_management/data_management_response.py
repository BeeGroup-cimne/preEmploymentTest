import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Llegim i filtrem files i columnes del fitxer que conté les dades
file_path = 'data_management/data_2019.xls'
df = pd.read_excel(file_path, usecols=lambda x: 'Unnamed' not in x)
df = df.dropna()

# Convertim columnes a date
df['d_ini'] = pd.to_datetime(df['d_ini'])
df['d_end'] = pd.to_datetime(df['d_end'])

# Definim rang de dates a treballar i creem un df amb les dates (redundant, pero permet cobrir el gap 1/1/2019-10/1/2019)
start = min(pd.to_datetime('2019-01-01'), df['d_ini'].min())
end = max(pd.to_datetime('2019-12-31'), df['d_end'].max())

daily_index = pd.date_range(start, end, freq='D')
ts_df = pd.DataFrame(index=daily_index)

# Calculem el promig de consum a cada ranc i afegin el resultat al df de dates
for index, row in df.iterrows():
    date_range = pd.date_range(start=row['d_ini'], end=row['d_end'], freq='D')
    average_kwh = row['kwh'] / len(date_range)
    ts_df.loc[date_range, 'kwh'] = average_kwh

# Mostrem resultats
print(ts_df)
    
plt.figure(figsize=(10, 6))
plt.plot(ts_df.index, ts_df['kwh'], label='Consum Promig Diari')
plt.title('Consum Electric Serie Temporal 2019')
plt.xlabel('Data')
plt.ylabel('Consum Promig Diari (kWh)')
plt.legend()
plt.grid(True)
plt.show()