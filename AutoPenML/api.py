from flask import Flask, request, jsonify
from scanner.nmap_scanner import run_nmap_scan
from scanner.feature_extractor import extract_features
from ml_model.vulnerability_predictor import predict_vulnerability
from reports.report_generator import generate_report
import os

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_target():
    data = request.get_json()
    target_ip = data.get('target_ip')

    if not target_ip:
        return jsonify({"error": "No target_ip provided"}), 400

    try:
        scan_data = run_nmap_scan(target_ip)
        features = extract_features(scan_data)
        prediction = predict_vulnerability(features)
        
        generate_report(target_ip, scan_data, prediction)
        
        return jsonify({
            "target_ip": target_ip,
            "open_ports_count": features['open_ports_count'],
            "os_type": features['os_type'],
            "vulnerable": bool(prediction),
            "report_path": f"reports/{target_ip.replace('.', '_')}_report.md"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Welcome to AutoPenML API! Use POST /scan with {'target_ip': 'IP_ADDRESS'}."

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)