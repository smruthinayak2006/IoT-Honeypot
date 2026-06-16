"""
IoT Honeypot Dashboard - Day 11 Upgrade
"""

import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DATABASE = "database/attacks.db"


def load_data():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM attacks",
        conn
    )

    conn.close()

    return df


st.title("IoT Honeypot Security Dashboard")

attacks = load_data()


# ----------------------------
# KPI SECTION
# ----------------------------
st.subheader("System Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Attacks", len(attacks))

with col2:
    st.metric("Unique IPs", attacks["ip_address"].nunique())

with col3:
    st.metric("Unique Usernames", attacks["username"].nunique())


# ----------------------------
# TABLE VIEW
# ----------------------------
st.subheader("Attack Logs")
st.dataframe(attacks)


# ----------------------------
# USERNAME CHART
# ----------------------------
st.subheader("Top Targeted Usernames")

username_counts = attacks["username"].value_counts()

fig1, ax1 = plt.subplots()
username_counts.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Attempts")
ax1.set_xlabel("Username")

st.pyplot(fig1)


# ----------------------------
# PASSWORD CHART
# ----------------------------
st.subheader("Most Tried Passwords")

password_counts = attacks["password"].value_counts()

fig2, ax2 = plt.subplots()
password_counts.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Attempts")
ax2.set_xlabel("Password")

st.pyplot(fig2)


# ----------------------------
# IP ANALYSIS
# ----------------------------
st.subheader("Top Attacking IPs")

ip_counts = attacks["ip_address"].value_counts().head(10)

fig3, ax3 = plt.subplots()
ip_counts.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Attempts")
ax3.set_xlabel("IP Address")

st.pyplot(fig3)