Day 6 Notes

Learned:

- Brute force detection
- Attack counting
- Python dictionaries
- Security alerts

Logic:

Multiple failed attempts from the same IP may indicate brute force behavior.

Additional Concepts:

False Positive:
When a security system incorrectly marks normal activity as an attack.

Detection Logic:
One failed login is normal.
Repeated failed attempts from the same IP indicate suspicious behavior.

Current Limitation:
Attack count is stored in RAM and resets after restarting the program.