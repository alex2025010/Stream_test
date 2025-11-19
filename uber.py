import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in New York City")

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
	'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATE_COLUMN = "date/time"

def load_data(nrows):
	data=pd.read_csv(DATA_URL,nrows=nrows)
	lowercase=lambda x: str(x).lower()
	data.rename(lowercase,axis="colums",inplace=True)
	data[DATE_COLUMNS]=pd.to_datatime(data[DATE_COLUMN])
	return data

data_load_state=st.text("Loading Data...")
data=load_data(10000)
data_load_state=st.text("Loading Data...Done!")