import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Yongyi Ren')
df = pd.read_csv(Path(__file__).resolve().parent / 'housing.csv')

# create a slider
house_value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)  # min, max, default

st.subheader('See more filters in the sidebar:')

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_filter = st.sidebar.radio(
     'Choose income level',
     ['Low', 'Medium', 'High'])

# filter by median house value
df = df[df.median_house_value >= house_value_filter]

# filter by location type
df = df[df.ocean_proximity.isin(location_filter)]

# filter by income level
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 4.5]

# show on map
st.map(df)

# show the plot
st.subheader('Distribution of Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))
ax.hist(df.median_house_value, bins=30)
ax.set_xlabel('Median House Value (USD)')
ax.set_ylabel('Number of Districts')
st.pyplot(fig)