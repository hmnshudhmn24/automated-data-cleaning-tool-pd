import streamlit as st
import pandas as pd
import pandas_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Title
st.title("🧹 Automated Data Cleaning and Profiling Tool")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📋 Raw Data Preview")
        st.dataframe(df.head())

        # Cleaning Options
        st.subheader("🛠 Cleaning Options")
        if st.checkbox("Drop rows with missing values"):
            df = df.dropna()
        if st.checkbox("Fill missing values with 'Unknown' (for object types)"):
            obj_cols = df.select_dtypes(include='object').columns
            df[obj_cols] = df[obj_cols].fillna('Unknown')
        if st.checkbox("Fill missing values with median (for numeric types)"):
            num_cols = df.select_dtypes(include='number').columns
            for col in num_cols:
                df[col] = df[col].fillna(df[col].median())

        st.success("✅ Cleaning done!")

        # Export cleaned data
        st.subheader("⬇️ Export Cleaned Data")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download cleaned CSV",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv',
        )

        # Profiling Report
        st.subheader("📊 Data Profiling Report")
        profile = ProfileReport(df, explorative=True)
        st_profile_report(profile)

    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("👆 Please upload a file to get started.")
