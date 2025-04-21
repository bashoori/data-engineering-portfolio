# 🚀 Data Engineering Portfolio 

Welcome to my Data Engineering Portfolio — a collection of real-world, cloud-native projects that demonstrate my skills in data pipelines, cloud architecture, automation, and analytics.

I’m a Data Engineer with 6+ years of experience across enterprise environments and freelance projects, specializing in Python, SQL, AWS, Airflow, and end-to-end data workflows. These projects highlight my passion for scalable infrastructure, automation, and delivering insights through clean data systems.

---

## 📂 Projects

### 🏥 [Healthcare FHIR Data Pipeline](./healthcare-FHIR-data-pipeline/)
**Tech:** Python • SQLite • BigQuery • Streamlit • GitHub Actions  
**Summary:**  
Simulates and processes healthcare data using FHIR standard. Parses patient, encounter, condition, and observation data from JSON, loads into SQLite and BigQuery, and visualizes insights using Streamlit.

- ✅ Simulated FHIR data via [Synthea](https://github.com/synthetichealth/synthea)
- ✅ Parsed JSON into normalized CSVs using Python
- ✅ Loaded into SQLite and BigQuery
- ✅ Created dashboards with Streamlit
- ✅ CI/CD with GitHub Actions

📎 [Live Streamlit Demo – Patients](https://probable-carnival-7wwr7r9xv9j2vgv-8501.app.github.dev/)  
📎 [Live Streamlit Demo – Conditions](https://probable-carnival-7wwr7r9xv9j2vgv-8502.app.github.dev/)  

---

### ☁️ [AWS Lambda Job Scraper](./AWS-lambda-linkedIn-scraper/)
**Tech:** Python • AWS Lambda • S3 • DynamoDB • SNS • EventBridge  
**Summary:**  
Scrapes LinkedIn guest search results for "Data Engineer" jobs in Vancouver. Saves job listings to S3, logs metadata to DynamoDB, and sends notifications via SNS.

- ✅ Runs serverless on AWS Lambda
- ✅ Parses job listings using BeautifulSoup
- ✅ Stores CSV files to S3 (Free Tier)
- ✅ Logs job scrape metadata to DynamoDB
- ✅ Sends email alerts via SNS
- ✅ Scheduled via EventBridge

📎 [Lambda Function Setup Guide](./AWS-lambda-linkedIn-scraper/lambda/README.md)

---

### 🛍️ [eBay to Google Sheets & Telegram](./Upwork-Projects/eBay-Product-Scraper/)
**Tech:** Python • gspread • Telegram API • BeautifulSoup  
**Summary:**  
Scrapes eBay search results, extracts top product info, appends to a Google Sheet, and sends a summary via Telegram.

- ✅ Uses Google Sheets API with OAuth
- ✅ Telegram bot alert on new items
- ✅ Deduplicates and timestamps entries
- ✅ Includes configurable search limit and sort options

---

## 🧠 Skills Demonstrated

- Cloud & Big Data: AWS (Lambda, S3, DynamoDB, Redshift, Glue), Google BigQuery  
- Programming: Python, SQL, Shell scripting  
- Automation: Apache Airflow, GitHub Actions, EventBridge  
- ETL Pipelines: API ingestion, FHIR data parsing, batch and stream processing  
- Dashboards: Streamlit, Looker Studio  
- Communication: GitHub documentation, SNS alerts, Confluence-style notes

---

## 📬 Let's Connect

- 🌐 [LinkedIn](https://www.linkedin.com/in/bashoori/)
- 🗂️ [More Projects Coming Soon!]

---

> ✨ *Built with love, cloud, and curiosity.*  