# Day 18 Notes

## Topic
Attacker IP Blocking System


## Implemented

- Created attacker blocking mechanism
- Added blocked IP storage
- Connected brute force detection with blocking
- Prevented blocked attackers from reconnecting


## Previous Workflow

Attack Attempt

        |

Detection

        |

Security Alert


The attacker could still continue trying.


## New Workflow

Attack Attempt

        |

Brute Force Detection

        |

Security Alert

        |

Store Blocked IP

        |

Reject Future Connections


## Database Update

Added:

blocked_ips table


Stores:

- ID
- IP Address
- Timestamp


## Files Updated


honeypot/database.py

Added:

- block_ip()
- is_blocked()


honeypot/detector.py

Added:

- automatic blocking after detection


honeypot/server.py

Added:

- blocked IP checking before allowing connection


## Concepts Learned

- Automated security response
- IP blocking
- Threat prevention
- Persistent blacklist storage


## Result

Successfully detected brute force attacks and automatically blocked suspicious IP addresses.