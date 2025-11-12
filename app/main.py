import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# PAGE SETUP
# -------------------------------
st.set_page_config(page_title="Solar Energy Dashboard", layout="wide")
st.title("🌞 Solar Energy Dashboard")
st.write("Compare solar metrics across countries or upload your own datasets.")

# -------------------------------
# FILE SOURCES
# -------------------------------
DATA_PATH = "data"

# Built-in country datasets (only if available locally)
available_countries = []
if os.path.exists(DATA_PATH):
    for file in os.listdir(DATA_PATH):
        if file.endswith("_clean.csv"):
            country = file.replace("_clean.csv", "").capitalize()
            available_countries.append(country)

# -------------------------------
# SIDEBAR OPTIONS
# -------------------------------
st.sidebar.header("⚙️ Dashboard Controls")
data_option = st.sidebar.radio(
    "Choose data source:",
    ["Use built-in country data", "Upload your own CSVs"]
)

# -------------------------------
# LOAD DATA
# -------------------------------
dfs = {}

if data_option == "Use built-in country data":
    if not available_countries:
        st.warning("No built-in cleaned data found in 'data/' folder.")
    else:
        selected_countries = st.sidebar.multiselect(
            "Select countries to analyze:",
            available_countries,
            default=available_countries[:1]
        )

        for country in selected_countries:
            file_path = os.path.join(DATA_PATH, f"{country.lower()}_clean.csv")
            try:
                dfs[country] = pd.read_csv(file_path)
            except Exception as e:
                st.error(f"Could not load {country}: {e}")

else:
    uploaded_files = st.sidebar.file_uploader(
        "Upload one or more cleaned CSV files",
        type=["csv"],
        accept_multiple_files=True
    )
    if uploaded_files:
        for file in uploaded_files:
            country = os.path.splitext(file.name)[0].capitalize()
            try:
                dfs[country] = pd.read_csv(file)
            except Exception as e:
                st.error(f"Error reading {file.name}: {e}")

# -------------------------------
# DATA VISUALIZATION
# -------------------------------
if dfs:
    st.subheader("📊 Metric Comparison Across Datasets")

    # Combine all datasets with a "Country" column
    combined = pd.concat(
        [df.assign(Country=name) for name, df in dfs.items()],
        ignore_index=True
    )

    # Drop rows missing solar columns
    solar_cols = ["GHI", "DNI", "DHI"]
    combined = combined.dropna(subset=solar_cols, how="all")

    # --- Boxplots ---
    for metric in solar_cols:
        if metric in combined.columns:
            st.write(f"### {metric} Comparison by Country")
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.boxplot(data=combined, x="Country", y=metric, palette="viridis", ax=ax)
            ax.set_title(f"{metric} Distribution by Country")
            st.pyplot(fig)

    # --- Summary Table ---
    st.write("### Summary Statistics (Mean, Median, Std)")
    summary = combined.groupby("Country")[solar_cols].agg(["mean", "median", "std"])
    st.dataframe(summary)

else:
    st.info("👆 Choose a data source and upload/select at least one dataset to begin.")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Developed for Solar Challenge Week 0 🌞 | Streamlit Dashboard Example")
