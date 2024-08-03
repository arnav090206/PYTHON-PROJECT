import streamlit as st
from file_handling import load_data, write_summary
from data_cleaning import clean_data
from data_visualization import visualize_data
import pandas as pd

st.title("_Milk Quality Analysis_")
st.subheader("_Milk quality analysis is a crucial process in the dairy industry, encompassing a range of tests and evaluations to ensure that milk meets health, safety, and quality standards. This analysis is vital for several reasons._")
st.write("----------------------------------------------------")
st.write("-----------------------------------------------")

# Load data
file_path = 'milknew.csv'
data = load_data(file_path)

# Clean data
cleaned_data = clean_data(data)

# Display data
if not cleaned_data.empty:
    st.write("### _Cleaned Data:_")
    st.dataframe(cleaned_data)
    st.write("-----------------------------------------------")

    # Perform visualizations
    visualize_data(cleaned_data)

    # Write summary
    write_summary(cleaned_data)
    file=pd.read_csv('summary.txt')
   

else:
    st.warning("_No data to display_")