import os

def generate_report(target_ip, scan_data, prediction):
    ports = list(scan_data['tcp'].keys()) if 'tcp' in scan_data else []
    os_guess = scan_data['osmatch'][0]['name'] if 'osmatch' in scan_data and scan_data['osmatch'] else 'Unknown'

    report = f"""
# AutoPenML Report
**Target**: {target_ip}

## Scan Summary:
- Open Ports: {ports}
- OS Guess: {os_guess}

## Machine Learning Prediction:
- Vulnerable: {"Yes" if prediction == 1 else "No"}

---
"""
    os.makedirs('reports', exist_ok=True)
    with open(f'reports/{target_ip.replace(".", "_")}_report.md', 'w') as f:
        f.write(report)

    print(f"[+] Report saved to 'reports/{target_ip.replace('.', '_')}_report.md'")