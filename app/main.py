import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from utils import load_data

st.title("Solar Energy Dashboard")
st.write("Explore and compare solar irradiance data across Benin, Sierra Leone, and Togo.")

# --- Load Data ---

countries = ["Benin", "SierraLeone", "Togo"]
country = st.selectbox("Select a country:", countries)

df = load_data(country)

if df is not None:
    st.write(f"### Preview of {country} data")
    st.dataframe(df.head())

    # --- Basic Stats ---
    st.write("### Summary Statistics")
    st.write(df.describe())

    # --- Boxplot ---
    st.write("### Distribution of Solar Irradiance")
    fig, ax = plt.subplots()
    sns.boxplot(data=df[["GHI", "DNI", "DHI"]])
    st.pyplot(fig)
else:
    st.warning("Please make sure your cleaned CSVs are in the 'data/' folder.")
