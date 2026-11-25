# Network Anomaly Intrusion Detection System (IDS)

A Machine Learning-based Intrusion Detection System leveraging Python and `scikit-learn`'s Isolation Forest algorithm to detect zero-day network behavioral anomalies.

## 📖 Complete Brief
Traditional signature-based IDS systems (like Snort or Suricata) fail against novel attacks because they rely on predefined dictionaries of known threats. This project takes a behavioral approach. Using the Isolation Forest algorithm, it analyzes continuous network flow telemetry (e.g., packet sizes, inter-arrival times, error rates) to establish a baseline of "normal" network operations. Any traffic pattern that drastically deviates from this learned baseline—such as a sudden flood of small packets (DDoS) or rapid, sequential port queries (Port Scanning)—is isolated and flagged as anomalous, making it highly effective against zero-day threats.

## ✨ Features
- **Machine Learning Flow Analysis:** Uses `IsolationForest` to handle multi-dimensional telemetry data and find outliers without relying on threat signatures.
- **Unsupervised Learning:** Does not require explicitly labeled "malware" data to train; it simply learns what "normal" looks like and flags the rest.
- **Mock Data Generation:** Includes a built-in telemetry generator that produces both benign data clusters and malicious outliers for immediate testing.

## 🛠 Prerequisites
- Python 3.x
- `numpy`
- `scikit-learn`

## 🚀 How to Run

1. **Navigate to the IDS directory:**
   ```bash
   cd ./network-anomaly-ids/
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the detector pipeline:**
   ```bash
   python3 ids_model.py
   ```

4. **Expected Output:**
   The script instantly generates mock network traffic telemetry, trains the unsupervised Isolation Forest model, and scores the dataset to reveal the simulated malicious packets:
   ```text
   [*] Generating network flow telemetry...
   [*] Training Isolation Forest Anomaly Detector...
   [*] Scoring traffic...
   [!] Detected 53 malicious network flows based on telemetry outliers.
   Example Malicious Packet Signature (Size, Interval, Error Rate): [1.458e+03 6.134e-04 9.173e-02]
   ```
