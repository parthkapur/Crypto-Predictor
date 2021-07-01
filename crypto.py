#importing the libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import MinMaxScaler

#making the streamlit page

st.set_page_config(layout="wide")
st.write('''
# Cryto-Currency Predcitor
''')

#getting the html

crypto = st.selectbox('Which Crpyto-Currency would you like to be predicted?', ('BTC', 'ETH', 'DOGE', 'USDT', 'BNB', 'ADA', 'XRP', 'USDC', 'DOT1', 'HEX', 'UNI3', 'BCH', 'LTC', 'SOL1',
                                                                                'LINK', 'MATIC', 'ETC', 'THETA', 'ICP1', 'XLM', 'VET', 'FIL', 'TRX', 'XMR', 'EOS', 'SHIB', 'AAVE', 'CRO',
                                                                               'BSV', 'ALGO', 'MKR', 'XTZ', 'LUNA1', 'ATOM1', 'AMP1', 'NEO', 'MIOTA', 'TFUEL', 'AVAX', 'DCR', 'CCXX',
                                                                               'HBAR', 'COMP', 'BTT1', 'KSM', 'WAVES', 'GRT2', 'TUSD', 'RUNE', 'CTC1', 'ZEC'))
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
df1=df.reset_index()['Close*']
df1 = df1.str.replace(',', '').astype(float)
scaler=MinMaxScaler(feature_range=(0,1))
df1=scaler.fit_transform(np.array(df1).reshape(-1,1))

