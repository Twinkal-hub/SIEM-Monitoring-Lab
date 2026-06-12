
# SIEM-Monitoring-Lab

## Overview

This project demonstrates basic Security Information and Event Management (SIEM) concepts by analyzing authentication logs using Python. The goal is to detect suspicious activity and identify potential brute-force attacks.

## Objective

Analyze authentication logs and detect repeated failed login attempts that may indicate malicious activity.

## Tools Used

- Python 3
- VS Code
- Windows PowerShell
- GitHub

## Project Structure

```
SIEM-Monitoring-Lab
│
├── logs
│     └── sample-auth.log
│
├── reports
│     └── incident-report.md
│
├── python-log-analyzer.py
├── README.md
├── LICENSE
└── .gitignore
```

## Log Source

The project uses sample SSH authentication logs containing failed and successful login attempts.

Example:

```
Jun 10 10:01:25 server sshd[1234]: Failed password for root from 192.168.1.100
Jun 10 10:02:11 server sshd[1235]: Failed password for admin from 192.168.1.100
```

## Detection Logic

The Python script:

- Reads authentication logs
- Extracts source IP addresses
- Counts login attempts
- Detects suspicious behavior
- Generates alerts when thresholds are exceeded

## Sample Output

```
========================================
        SIEM Security Report
========================================

Failed Login Attempts

192.168.1.100 : 4
192.168.1.101 : 1
192.168.1.102 : 1

Threat Detection

[HIGH] Possible Brute Force Attack
Source IP : 192.168.1.100
Reason    : Failed login threshold exceeded

========================================
```

## Findings

- Multiple failed login attempts were identified.
- IP address 192.168.1.100 exceeded the threshold.
- Activity may indicate a brute-force attack.

## Recommendations

- Implement account lockout policies.
- Enable Multi-Factor Authentication (MFA).
- Block suspicious IP addresses.
- Continuously monitor authentication logs.

## Skills Demonstrated

- Log Analysis
- Threat Detection
- Brute Force Identification
- Python Automation
- Incident Investigation
- Security Monitoring
- SIEM Concepts
- Cybersecurity Reporting

## Future Improvements

- Export reports to CSV
- Add timestamp analysis
- Add suspicious IP blacklist
- MITRE ATT&CK mapping
- Wazuh integration
- Splunk dashboard integration

**Author:** Twinkal Rana  
**Focus Areas:** SOC Analyst | Cybersecurity Analyst | SIEM Monitoring | Blue Team
