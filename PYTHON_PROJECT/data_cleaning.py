





















'''Group 10:
Rushikesh Chougule
Suyash Bhosale
Arnav Warkar
Sarthak Gavhane'''

import pandas as pd
import streamlit as st
from exception_handling import handle_exception

def clean_data(data):
    try:
        data = data.dropna()
        data = data.drop_duplicates()
        return data
    except Exception as e:
        handle_exception(e)
        return pd.DataFrame()  