# Incident Report

## Objective

Analyze authentication logs to detect suspicious login activity and possible brute-force attacks.

## Findings

- Multiple failed login attempts were identified.
- IP address 192.168.1.100 generated four failed authentication attempts.
- Activity exceeded the predefined threshold.

## Risk Assessment

The repeated failures indicate a possible brute-force attack against the SSH service.

## Recommendations

- Enable account lockout policies.
- Implement multi-factor authentication (MFA).
- Block suspicious IP addresses.
- Continuously monitor authentication logs.

## Conclusion

The investigation identified suspicious authentication activity that may indicate brute-force attempts. Additional monitoring and preventive controls are recommended.
