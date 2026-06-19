"""
IoT Honeypot Security Dashboard
"""

import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import sys


sys.path.append(
    "honeypot"
)


from report import generate_report
from database import unblock_ip

DATABASE = "database/attacks.db"


# -----------------------------
# DATABASE FUNCTIONS
# -----------------------------

def load_attacks():

    conn = sqlite3.connect(DATABASE)

    data = pd.read_sql_query(
        "SELECT * FROM attacks",
        conn
    )

    conn.close()

    return data



def load_alerts():

    conn = sqlite3.connect(DATABASE)

    data = pd.read_sql_query(
        "SELECT * FROM alerts",
        conn
    )

    conn.close()

    return data



# -----------------------------
# LOAD DATA
# -----------------------------

attacks = load_attacks()

alerts = load_alerts()


# -----------------------------
# DASHBOARD
# -----------------------------

st.title(
    "IoT Honeypot Security Dashboard"
)


st.subheader(
    "System Overview"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Attacks",
        len(attacks)
    )


with col2:

    st.metric(
        "Unique Attackers",
        attacks["ip_address"].nunique()
    )


with col3:

    st.metric(
        "Security Alerts",
        len(alerts)
    )



# -----------------------------
# ALERT SECTION
# -----------------------------

st.subheader(
    "🚨 Security Alerts"
)


if len(alerts) > 0:


    st.warning(
        "Threat activity detected!"
    )


    st.dataframe(
        alerts
    )


else:


    st.success(
        "No threats detected"
    )



# -----------------------------
# ATTACK LOGS
# -----------------------------

st.subheader(
    "Attack Records"
)


st.dataframe(
    attacks
)



# -----------------------------
# USERNAME CHART
# -----------------------------

st.subheader(
    "Top Usernames"
)


fig1, ax1 = plt.subplots()


attacks["username"].value_counts().plot(
    kind="bar",
    ax=ax1
)


st.pyplot(
    fig1
)



# -----------------------------
# PASSWORD CHART
# -----------------------------

st.subheader(
    "Top Passwords"
)


fig2, ax2 = plt.subplots()


attacks["password"].value_counts().plot(
    kind="bar",
    ax=ax2
)


st.pyplot(
    fig2
)

# -----------------------------
# REPORT GENERATION
# -----------------------------


st.subheader(
    "Generate Security Report"
)


if st.button(
    "Generate Report"
):


    report_file = generate_report()


    with open(
        report_file,
        "rb"
    ) as file:


        st.download_button(

            label="Download Report",

            data=file,

            file_name="honeypot_report.csv",

            mime="text/csv"
        )

# -------------------------
# BLOCKED IPS
# -------------------------

st.subheader(
    "Blocked Attackers"
)


connection = sqlite3.connect(
    "database/attacks.db"
)


blocked = pd.read_sql_query(
    "SELECT * FROM blocked_ips",
    connection
)


st.dataframe(
    blocked
)


if len(blocked) > 0:


    selected_ip = st.selectbox(
        "Select IP to unblock",
        blocked["ip_address"]
    )


    if st.button(
        "Unblock IP"
    ):


        unblock_ip(
            selected_ip
        )


        st.success(
            "IP Unblocked Successfully"
        )


connection.close()