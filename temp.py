import pandas as pd
import streamlit as st
import requests
import time

st.title('FMMS')
st.header('Temp Data')
df = pd.read_csv('temp.csv')
chart = st.line_chart(df, x='Date/Time', y='Temperature')
while True:
 value = requests.get('https://api.init.st/data/v1/events/latest?accessKey=ist_ZvMxedzZJYVKw5ZYEYzvPyZfuj03rmVi&bucketKey=Y8TK3CE9SPU5', timeout=2)
 value = value.json()['temperature (C)']['value']

 dic = {'Date/Time': time.asctime(time.localtime())[4:19], 'Temperature': value}
 
 df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
 
 df.to_csv('temp.csv',index=False)
 chart.empty()
 chart = st.line_chart(df, x='Date/Time', y='Temperature')
 time.sleep(2)
