#importing the libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

#making the streamlit page

st.set_page_config(layout="wide")
st.write('''
# Cryto-Currency Predcitor
''')

#getting the html

crypto = st.selectbox('Which Crpyto-Currency would you like to be predicted?', ('BTC', 'ETH', 'DOGE'))
url = "https://finance.yahoo.com/quote/" + crypto + "-USD/history?p=" + crypto + "-USD"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table_data = soup.find('table', attrs={'data-test': 'historical-prices'})
headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)
    
df = pd.DataFrame(columns = headers)
for row in table_data.find_all('tr')[1:100]:
    data = row.find_all('td')
    row_data = [td.text for td in data]
    length = len(df)
    df.loc[length] = row_data
st.dataframe(df)