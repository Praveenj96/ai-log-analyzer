from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(log_lines):
    df = pd.DataFrame(log_lines, columns=["log"])
    df["length"] = df["log"].apply(len)

    model = IsolationForest(contamination=0.3, random_state=42)
    df["anomaly"] = model.fit_predict(df[["length"]])

    return df
