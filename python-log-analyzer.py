from collections import Counter
import re

ip_addresses = []

with open("logs/sample-auth.log", "r") as file:
    for line in file:
        match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip_addresses.append(match.group(1))

counter = Counter(ip_addresses)

print("===== Security Analysis Report =====")

for ip, count in counter.items():
    print(f"{ip} -> {count} failed login attempts")

print("\nPotential Brute Force Detection:")

for ip, count in counter.items():
    if count >= 3:
        print(f"ALERT: {ip} exceeded threshold!")
