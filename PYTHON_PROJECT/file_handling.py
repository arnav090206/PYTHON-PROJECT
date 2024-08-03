import pandas as pd
import streamlit as st
from exception_handling import handle_exception

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return pd.DataFrame()
    except Exception as e:
        handle_exception(e)
        return pd.DataFrame()
    else:
        st.success("_File loaded successfully!_")
        return data

def write_summary(data):
    try:
        with open('summary.txt', 'w') as file:
            highest_quality = data.max()
            lowest_quality = data.min()
            file.write(f"Highest Quality: {highest_quality}\n")
            file.write(f"Lowest Quality: {lowest_quality}\n")
            
        
    except Exception as e:
        handle_exception(e)