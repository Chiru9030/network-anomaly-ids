# Network Anomaly IDS (Machine Learning)

An Unsupervised Machine Learning model that detects network intrusions without needing static malware signatures.

## Architecture
Uses Scikit-Learn's `IsolationForest` algorithm. Unlike standard classifiers that require labeled attack data, the Isolation Forest isolates outliers in multi-dimensional space. By feeding it network flow telemetry (Packet Size, Arrival Times, Error Rates), it mathematically flags volumetric attacks (DDoS) and aggressive recon (Port Scans).

## Usage
```bash
pip install -r requirements.txt
python ids_model.py
```
