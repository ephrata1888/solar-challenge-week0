# 🌞 Solar Challenge Week 0 — MoonLight Energy Solutions

## 📘 Overview
This project was developed as part of the **10 Academy Week 0 Challenge**.  
The goal is to analyze solar radiation data from **Benin**, **Sierra Leone**, and **Togo**, perform data cleaning and exploratory data analysis (EDA), compare solar potential across regions, and build an **interactive Streamlit dashboard**.

---

## 🎯 Objectives
- Profile, clean, and explore solar datasets for each country.
- Identify patterns and anomalies in irradiance, temperature, and humidity.
- Compare regions based on solar potential metrics (GHI, DNI, DHI).
- Create an interactive dashboard to visualize solar insights.
- Demonstrate good Git practices and project structure.

---

## 🧩 Folder Structure
```
solar-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py              # Streamlit dashboard
├── data/
│   ├── benin_clean.csv
│   ├── sierra_clean.csv
│   └── togo_clean.csv
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_eda.ipynb
│   └── togo_eda.ipynb
├── scripts/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Environment Setup

### 1️⃣ Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Jupyter notebooks
All data cleaning and EDA steps are performed in the notebooks under the `notebooks/` directory.

---

## 🧠 Data Analysis Summary

### 📍 Task 1 — Setup
- Created and configured the GitHub repo.
- Added `.gitignore`, `requirements.txt`, and CI workflow.
- Set up a virtual environment and dependencies.

### ☀️ Task 2 — Data Profiling, Cleaning & EDA
- Analyzed solar datasets from **Benin**, **Sierra Leone**, and **Togo**.
- Checked for missing values, outliers, and data consistency.
- Imputed missing values and removed extreme outliers using Z-scores.
- Exported cleaned data to `/data` (ignored in `.gitignore`).

### 📊 Task 3 — Country Comparison
- Compared GHI, DNI, DHI across countries using boxplots and summary stats.
- Conducted an ANOVA test to check if GHI differences were statistically significant.
- Key findings:
  - **Benin** showed the highest average GHI and variability.
  - **Sierra Leone** had lower irradiance but more consistent readings.
  - **Togo** ranked second in mean GHI, showing stable solar potential.

### 💻 Task 4 — Streamlit Dashboard
An interactive dashboard was built to visualize the data dynamically.

---

## 🚀 Run the Streamlit Dashboard

### 1️⃣ Activate environment
```bash
.venv\Scripts\activate
```

### 2️⃣ Run the app
```bash
streamlit run app/main.py
```

### 3️⃣ Open in browser
Streamlit will display a link like:
```
http://localhost:8501
```

---

## 🎨 Dashboard Features
- **Dropdown menu** to select a country.
- **Interactive boxplots** for GHI, DNI, and DHI.
- **Summary statistics** for the selected dataset.
- Future enhancements: top regions ranking, correlation analysis, and time-based filters.

---

## 🧾 Requirements
Main Python libraries used:
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **scipy**
- **streamlit**

---

## 📚 Insights
- Higher GHI values suggest **Benin** has greater solar energy potential.
- **Sierra Leone** exhibits lower solar radiation, likely due to higher humidity levels.
- **Togo** provides balanced conditions suitable for consistent solar harvesting.

---

## 🔗 Repository
**GitHub Repository:** [https://github.com/ephrata1888/solar-challenge-week0]

---

## 👩‍💻 Author
**Efrata Wolde**  
Week 0 — Solar Challenge Participant  
10 Academy | Data, AI & Engineering Training
