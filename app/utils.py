import pandas as pd
import os
import streamlit as st

@st.cache_data
def load_data(country):
    """Load cleaned data for a given country."""
    file_path = f"data/{country.lower()}_clean.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.error(f"Data for {country} not found at {file_path}")
        return None
