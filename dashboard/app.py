"""
IoT Honeypot Dashboard
"""

import streamlit as st

import sqlite3

import pandas as pd



DATABASE = "database/attacks.db"



def load_data():


    connection = sqlite3.connect(
        DATABASE
    )


    data = pd.read_sql_query(
        "SELECT * FROM attacks",
        connection
    )


    connection.close()


    return data



st.title(
    "IoT Honeypot Dashboard"
)


attacks = load_data()



st.subheader(
    "Attack Records"
)


st.dataframe(
    attacks
)

st.subheader(
    "Statistics"
)


st.write(
    "Total Attacks:",
    len(attacks)
)


st.write(
    "Most Tried Username:"
)


st.write(
    attacks["username"].value_counts()
)


st.write(
    "Most Tried Password:"
)


st.write(
    attacks["password"].value_counts()
)