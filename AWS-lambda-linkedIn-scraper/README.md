## 🚀 LinkedIn Job Scraper Pipeline (AWS Lambda)

This project deploys a serverless pipeline that scrapes job listings from LinkedIn, uploads the data to S3, logs metadata in DynamoDB, and sends SNS notifications — all using AWS Free Tier services.

---

### 🛠 Project Structure
```
.
├── lambda/
│   └── handler.py             # Lambda entry point
├── lambda_layer/              # Temporary folder for packaging
├── sns_setup.py               # One-time setup: Create SNS topic + subscribe
├── dynamodb_setup.py          # One-time setup: Create DynamoDB table
├── requirements.txt           # Dependencies
├── .env.example               # Template for environment variables
├── .gitignore                 # Ignore sensitive and build files
└── .github/workflows/
    └── deploy-lambda.yml      # GitHub Actions deploy script
```

---

### 🧪 Local Setup
1. Clone the repo
2. Rename `.env.example` → `.env` and fill in credentials
3. Run setup scripts:
   ```bash
   python dynamodb_setup.py
   python sns_setup.py
   ```
4. Test your handler:
   ```bash
   python lambda/handler.py
   ```

---

### 🚀 GitHub Actions: Auto Deployment
This repo includes a GitHub Actions workflow that packages your Lambda and deploys it when triggered manually.

#### ✅ Prerequisites:
- Set GitHub Secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

#### ▶️ To Deploy:
- Go to **GitHub → Actions → Deploy Lambda → Run Workflow**

---

### 🗓 Optional: Automate with EventBridge
You can automate the Lambda to run daily:
1. Go to AWS Console → Amazon EventBridge
2. Create a new rule with a schedule (e.g., every 24 hours)
3. Target → Lambda function → `linkedin-job-scraper`

---

### ✅ AWS Services Used (Free Tier)
- **S3** – Data storage
- **DynamoDB** – Logging run history
- **SNS** – Email notifications
- **Lambda** – Core scraper
- **EventBridge** – Daily automation

---

### 📧 Output
- CSV files in S3 (`linkedin/YYYYMMDD_HHMM.csv`)
- Logs in DynamoDB (`JobScraperLogs`)
- Alert email when job list is uploaded

---

### 📌 License
MIT License — free to use, modify, and distribute.

---

### 🙋‍♀️ Author
Made by Bita — Data Engineer & Cloud Enthusiast
