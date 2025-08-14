# Cloud-Based Financial Analytics Dashboard

An interactive Streamlit dashboard hosted on AWS EC2 with secure file storage on AWS S3.

## Features
- Upload and preview CSV files
- Store uploaded files in S3 (via boto3)
- Retrieve and visualize historical datasets from S3
- Ready for forecasting with Prophet

## Tech Stack
Python, Streamlit, Pandas, AWS EC2, AWS S3, boto3, Prophet, Ubuntu

## Run locally
pip install -r requirements.txt
streamlit run dashboard_app.py
