import numpy as np
from sklearn.ensemble import IsolationForest

def generate_mock_traffic_data(n_samples=1000):
    # Features: [packet_size, inter_arrival_time, error_rate]
    # Normal traffic (benign)
    normal_data = np.random.normal(loc=[500, 0.1, 0.01], scale=[100, 0.02, 0.005], size=(n_samples, 3))
    
    # Anomalous traffic (e.g., DDoS or Port Scan)
    anomaly_data = np.random.normal(loc=[1500, 0.001, 0.1], scale=[200, 0.0005, 0.05], size=(int(n_samples*0.05), 3))
    
    return np.vstack([normal_data, anomaly_data])

def train_and_detect():
    print("[*] Generating network flow telemetry...")
    X = generate_mock_traffic_data()
    
    print("[*] Training Isolation Forest Anomaly Detector...")
    # Isolation Forest isolates anomalies (rare metrics far from normal clusters)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    
    print("[*] Scoring traffic...")
    predictions = model.predict(X) # 1 for normal, -1 for anomaly
    
    anomalies = X[predictions == -1]
    print(f"[!] Detected {len(anomalies)} malicious network flows based on telemetry outliers.")
    print("Example Malicious Packet Signature (Size, Interval, Error Rate):", anomalies[0])

if __name__ == "__main__":
    train_and_detect()
