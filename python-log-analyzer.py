from collections import Counter
import re

ip_addresses = []

with open("logs/sample-auth.log", "r") as file:
    for line in file:
        match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip_addresses.append(match.group(1))

counter = Counter(ip_addresses)

print("=" * 40)
print("        SIEM Security Report")
print("=" * 40)

print("\nFailed Login Attempts\n")

for ip, count in counter.items():
    print(f"{ip} : {count}")

print("\nThreat Detection\n")

for ip, count in counter.items():
    if count >= 3:
        print("[HIGH] Possible Brute Force Attack")
        print(f"Source IP : {ip}")
        print("Reason    : Failed login threshold exceeded")

print("\n" + "=" * 40)
