import requests
import pandas as pd
import plotly.express as px

# Fetch the data
response = requests.get('https://btc-esp8266-1dd205c5725f.herokuapp.com/data/all')
data = response.json()  

df = pd.DataFrame(data)

df['price'] = df['price'].str.strip().astype(float)

df['timestamp'] = pd.to_datetime(df['timestamp']) 

df.sort_values('timestamp', inplace=True)

# Plot
fig = px.line(df, x='timestamp', y='price', title='Bitcoin Prices Over Time', markers=True)
fig.show()