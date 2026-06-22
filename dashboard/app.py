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

from threat_intel import analyze_threat
from report import generate_report
from database import unblock_ip
from auth import verify_login

# ==============================
# DASHBOARD AUTHENTICATION
# ==============================


if "login" not in st.session_state:


    st.session_state.login = False



if not st.session_state.login:


    st.title(
        "🔐 IoT Honeypot Login"
    )


    username = st.text_input(
        "Username"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button(
        "Login"
    ):


        if verify_login(
            username,
            password
        ):


            st.session_state.login = True


            st.rerun()


        else:


            st.error(
                "Invalid Credentials"
            )


    st.stop()



# ==============================
# ADMIN SIDEBAR
# ==============================


with st.sidebar:


    st.title(
        "🛡️ Admin Panel"
    )


    st.success(
        "System Online"
    )


    st.write(
        "Logged in as:"
    )


    st.code(
        "admin"
    )


    st.divider()


    st.subheader(
        "System Info"
    )


    st.write(
        "Service:"
    )


    st.write(
        "IoT Honeypot"
    )


    st.write(
        "Mode:"
    )


    st.write(
        "Monitoring"
    )


    st.divider()


    st.subheader(
        "Actions"
    )


    if st.button(
        "Logout"
    ):


        st.session_state.login = False


        st.rerun()


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

# -------------------------
# SECURITY LOG VIEWER
# -------------------------


st.subheader(
    "Security Event Logs"
)


try:


    with open(
        "logs/security.log",
        "r"
    ) as file:


        logs = file.readlines()


    recent_logs = logs[
        -20:
    ]


    for log in reversed(
        recent_logs
    ):


        if "CRITICAL" in log:


            st.error(
                log
            )


        elif "WARNING" in log:


            st.warning(
                log
            )


        else:


            st.info(
                log
            )



except FileNotFoundError:


    st.info(
        "No security logs available"
    )

    st.header(
    "Threat Intelligence"
)



# ------------------------------
# Threat Intelligence Section
# ------------------------------

st.header(
    "🧠 Threat Intelligence"
)


ip_list = attacks[
    "ip_address"
].unique()


selected_ip = st.selectbox(
    "Select attacker IP",
    ip_list
)


if selected_ip:


    threat = analyze_threat(
        selected_ip
    )


    st.subheader(
        "Threat Analysis Result"
    )


    st.write(
        "IP Address:",
        threat["ip"]
    )


    st.write(
        "Attempts:",
        threat["attempts"]
    )


    st.write(
        "Risk Level:",
        threat["risk"]
    )


    st.write(
        "Analysis:",
        threat["reason"]
    )