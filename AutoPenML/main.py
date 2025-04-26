from scanner.nmap_scanner import run_nmap_scan
from scanner.feature_extractor import extract_features
from ml_model.vulnerability_predictor import predict_vulnerability
from reports.report_generator import generate_report
from utils.helpers import clean_ip

def main():
    target_ip = input("Enter the target IP address: ")
    target_ip = clean_ip(target_ip)

    scan_data = run_nmap_scan(target_ip)
    features = extract_features(scan_data)
    prediction = predict_vulnerability(features)
    generate_report(target_ip, scan_data, prediction)

if __name__ == "__main__":
    main()