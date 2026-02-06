import streamlit as st
from model import detect_anomalies

st.set_page_config(page_title="AI Log Analyzer", layout="wide")
st.title("🧠 AI Log Analyzer & Anomaly Detection")

uploaded_file = st.file_uploader("Upload Log File", type=["txt"])

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8").splitlines()
    result = detect_anomalies(logs)

    st.subheader("🔍 Analysis Result")
    st.dataframe(result)

    st.success("Anomalies detected successfully!")
