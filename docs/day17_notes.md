# Day 17 Notes

## Topic
Dashboard Report Download System


## Implemented

- Added report generation option in dashboard
- Added CSV download feature
- Connected report generator with Streamlit UI


## Previous Workflow

Database
   |
   v

Python Script
   |
   v

CSV Report


Problem:

Reports had to be generated manually using commands.


## New Workflow

Security Dashboard
        |
        v

Generate Report Button
        |
        v

Create CSV Report
        |
        v

Download Report


## Why Dashboard Reports?

Dashboard-based reports allow security analysts to export attack evidence without running backend scripts.

It makes the honeypot easier to use.


## Files Modified

honeypot/report.py

Updated:
- generate_report() returns generated file path


dashboard/app.py

Added:
- Generate Report button
- Download CSV option


## Concepts Learned

- Security report automation
- Dashboard integration
- Evidence exporting
- User-friendly security tools


## Result

Successfully integrated attack report generation and download functionality into the IoT honeypot dashboard.