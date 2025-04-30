# 🚀 Data Engineering Portfolio 

Welcome to my Data Engineering Portfolio — a collection of hands-on, cloud-native projects that demonstrate my capabilities across data engineering, cloud infrastructure, and automation. With over 6 years of experience, I specialize in building scalable pipelines using Python, SQL, AWS, Airflow, and Google Cloud.

Each project below is designed to solve real-world problems and showcase modern data engineering practices.

---

## 📁 Featured Projects

### 🏥 [Healthcare FHIR Data Pipeline](./healthcare-FHIR-data-pipeline/)
**Tech:** Python • FHIR JSON • SQLite • BigQuery • Streamlit • GitHub Actions  
**Use Case:** Healthcare Data Simulation & Analysis

- 🔹 Parses simulated patient, condition, encounter, and observation data from [Synthea](https://github.com/synthetichealth/synthea)
- 🔹 Transforms and stores records in SQLite and BigQuery
- 🔹 Interactive dashboards via Streamlit
- 🔹 Modular design with reusable Python scripts
- 🔹 CI/CD enabled via GitHub Actions

📌 [Patients Dashboard](https://probable-carnival-7wwr7r9xv9j2vgv-8501.app.github.dev/)  
📌 [Conditions Dashboard](https://probable-carnival-7wwr7r9xv9j2vgv-8502.app.github.dev/)

---

### ☁️ [AWS Lambda LinkedIn Scraper](./AWS-lambda-linkedIn-scraper/)
**Tech:** Python • AWS Lambda • S3 • DynamoDB • SNS • EventBridge  
**Use Case:** Automated Job Scraper + Serverless Pipeline

- 🔹 Scrapes LinkedIn job listings for "Data Engineer" roles
- 🔹 Saves job info (CSV) to AWS S3
- 🔹 Logs metadata to DynamoDB
- 🔹 Sends alerts via Amazon SNS
- 🔹 EventBridge cron job for scheduling
- 🔹 Fully compliant with AWS Free Tier

📌 [Lambda Function Guide](./AWS-lambda-linkedIn-scraper/lambda/README.md)

---

### 📊 [eBay Product Tracker](./ebay-product-tracker/)
**Tech:** Python • gspread • Google Sheets API • Telegram Bot • BeautifulSoup  
**Use Case:** Affiliate/Product Monitoring Tool

- 🔹 Scrapes eBay product listings based on search terms
- 🔹 Pushes results into Google Sheets with timestamps
- 🔹 Sends Telegram alerts for daily deals or price drops
- 🔹 Includes sorting, deduplication, and rate control

---

### 💼 [LinkedIn Job Scraper (Guest API)](./linkedIn-job-scraper/)
**Tech:** Python • BeautifulSoup • Google Sheets • Telegram  
**Use Case:** Job Research & Alert System

- 🔹 Scrapes LinkedIn’s public job listings (no login required)
- 🔹 Filters for keywords like “Data Engineer” in specific regions
- 🔹 Sends new listings to Google Sheets + Telegram
- 🔹 Designed for job-seekers and career coaches

---

### 🧘 [VitalTrack – Wellness Pipeline (COMING SOON)](./vitaltrack-wellness-pipeline/)
**Tech:** Python • Fitbit API • SQLite/BigQuery • Looker Studio  
**Use Case:** Personal Wellness Dashboard (Sleep, Steps, Stress)

- 🔹 Connects to health wearables and collects daily vitals
- 🔹 Cleans and normalizes metrics for long-term trends
- 🔹 Exports to Looker Studio for visual wellness dashboards

🔧 *Under Development*

---

## 🧠 Key Skills Demonstrated

- **Cloud & Infrastructure:** AWS (Lambda, S3, Redshift, Glue, DynamoDB, EventBridge), GCP (BigQuery)
- **Data Pipelines:** ETL, streaming & batch workflows, API integrations
- **Programming:** Python, SQL, Shell scripting
- **Dashboards & Visualization:** Streamlit, Looker Studio, Google Sheets
- **Automation:** Apache Airflow, GitHub Actions, Serverless Framework
- **Communication:** GitHub README, Telegram alerts, Confluence-style documentation

---

## 📌 How to Use

```bash
# Clone the portfolio
git clone https://github.com/bashoori/data-engineering-portfolio.git

# Navigate to a project
cd healthcare-FHIR-data-pipeline

# Set up Python environment
pip install -r requirements.txt

# Run your pipeline!
python scripts/patients_parser.py