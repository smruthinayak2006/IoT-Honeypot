# Day 22 Notes

## Topic
Security Log Dashboard Viewer


## Implemented

- Integrated security logs into dashboard
- Added recent event monitoring
- Displayed log severity levels


## Previous Workflow

Security Event

        |

security.log file

        |

Manual checking


## New Workflow

Security Event

        |

security.log

        |

Dashboard Viewer


## Log Categories

INFO

Normal system activity


WARNING

Suspicious activity


CRITICAL

Confirmed security threat


## Files Updated

dashboard/app.py


Added:

- Security log reader
- Recent log display
- Severity based visualization


## Concepts Learned

- Log monitoring
- Security event visibility
- SOC dashboard workflow


## Result

Security analysts can now monitor system events directly from the dashboard.