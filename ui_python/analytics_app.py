import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


@st.cache
def load_and_process():
    data = pd.read_excel('../data_analysis/Canada.xlsx',skiprows=20, skipfooter=2)
    data.drop(columns=['Type','AREA','REG','DEV'], inplace=True)
    data.rename({
        'OdName':'Country',
        'AreaName':'Continent',
        'RegName' : 'Region',
        'DevName' : 'Status'
    }, axis=1, inplace=True)
    data['Total'] = data[range(1980,2014)].sum(axis=1)
    data.set_index('Country', inplace=True)
    return data

df = load_and_process
