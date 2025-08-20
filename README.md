![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange)
![AWS S3](https://img.shields.io/badge/AWS-S3-yellowgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

🔗 **Live Demo:** [http://13.61.186.142:8501](http://13.61.186.142:8501)
# Cloud-Based Financial Analytics Dashboard

An interactive Streamlit dashboard hosted on AWS EC2 with secure file storage on AWS S3.
# 📊 Cloud-Based Financial Analytics Dashboard  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B?logo=streamlit)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange?logo=amazonaws)
![AWS S3](https://img.shields.io/badge/AWS-S3-green?logo=amazonaws)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview  
An **interactive financial analytics dashboard** built with **Streamlit**, deployed on **AWS EC2**, and integrated with **AWS S3** for secure, cloud-based storage.  
Users can **upload**, **analyze**, and **retrieve** CSV datasets directly from the cloud. The app is also ready for **forecasting** using Facebook’s Prophet library.

---

## 🚀 Features  
- 📤 **Upload CSV** files via the dashboard  
- ☁️ **Automatic S3 storage** using `boto3`  
- 📂 **Retrieve & preview historical datasets** from AWS S3  
- 📊 Interactive data visualization in Streamlit  
- 📈 Ready for forecasting with **Prophet**  
- 🔒 Secure IAM roles & private bucket access  

---

## 🛠 Tech Stack  
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python 3.9+, Pandas, NumPy, Prophet  
- **Cloud Hosting**: AWS EC2 (Ubuntu)  
- **Cloud Storage**: AWS S3 (private bucket)  
- **Integration**: boto3 AWS SDK  

---

## 📦 Installation  

### 1️⃣ Clone the repo
```bash
git clone https://github.com/guntaaskaur31/Cloud-financial-dashboard.git
cd Cloud-financial-dashboard

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
