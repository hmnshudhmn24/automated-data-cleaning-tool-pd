# 🧹 Automated Data Cleaning and Profiling Tool

This project is a **Streamlit**-based web app that automatically **cleans, summarizes, and profiles** uploaded CSV or Excel files using **Pandas** and **YData Profiling**.

## 🎯 Features

- Upload `.csv` or `.xlsx` files
- Options to handle missing values (drop, fill with median, fill with 'Unknown')
- Quick data cleaning without coding
- Interactive data profiling report using YData Profiling (Pandas Profiling)
- Download cleaned dataset instantly

## 📦 Requirements

```bash
pip install pandas streamlit ydata-profiling streamlit-pandas-profiling openpyxl
```

## 🚀 How to Run

1. Install the required libraries.

2. Launch the Streamlit app:

```bash
streamlit run app/main.py
```

3. Upload your dataset and start cleaning and exploring it effortlessly!

## 📈 Output

- Cleaned dataset download option
- Full interactive EDA report

---

✨ Made with Pandas, Streamlit, and YData Profiling.
