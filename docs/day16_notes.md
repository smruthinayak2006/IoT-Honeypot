# Day 16 Notes

## Topic
Attack Report Generation


## Implemented

- Created CSV report generator
- Exported attack records from database
- Added automatic report folder creation
- Stored security evidence reports


## Workflow

SQLite Database
        |
        v

Fetch Attack Logs
        |
        v

Generate CSV Report
        |
        v

Save Report File


## Why Reports Are Needed

Security reports help analysts:
- Review previous attacks
- Preserve evidence
- Analyze attack patterns
- Share incident details


## Files Added

honeypot/report.py

Features:
- Reads attack database
- Creates reports folder
- Generates timestamped CSV reports


tests/generate_report.py

Used to test report generation


## Concepts Learned

- Security reporting
- Evidence collection
- CSV log exporting
- Automated file generation


## Result

Successfully generated attack reports containing captured honeypot activity.