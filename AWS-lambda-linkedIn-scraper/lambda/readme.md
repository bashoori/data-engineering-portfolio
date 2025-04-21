# 🧠 Lambda Function: LinkedIn Job Scraper

This folder contains the core Lambda function `handler.py`, which is responsible for scraping LinkedIn job listings, saving the data to an S3 bucket, and logging the job run in DynamoDB.

---

## 📂 Files

- `handler.py` – Main AWS Lambda entry point
- This function is zipped and deployed automatically via GitHub Actions

---

## ⚙️ Lambda Environment Variables
Set these variables when creating or configuring the Lambda in AWS:

```env
AWS_REGION=us-west-2
S3_BUCKET_NAME=bashoori-s3
DYNAMODB_TABLE=JobScraperLogs
SNS_TOPIC_ARN=arn:aws:sns:us-west-2:123456789012:LinkedInJobAlerts
```

These should match the `.env.example` file used for local testing.

---

## 📦 Deployment Notes
This function is zipped using GitHub Actions and pushed to AWS Lambda. To run it manually:

1. Go to AWS Lambda Console
2. Find `linkedin-job-scraper`
3. Click **Test** or set up a CloudWatch or EventBridge trigger

---

## 📝 Function Workflow

1. Scrape LinkedIn job cards for a keyword (e.g., `Data Engineer`)
2. Extract job title, company, location, link, and timestamp
3. Save the result as a `.csv` file to S3
4. Log the event in DynamoDB with job count and timestamp
5. Send a notification via SNS (email)

---

## ✅ Output Example (S3 CSV)
```csv
Title,Company,Location,Link,Timestamp
"Data Engineer","Amazon","Vancouver, BC","https://linkedin.com/...","2024-04-01 10:00"
```

---

## 🔐 IAM Permissions Required
Attach a role to this Lambda with permissions:

- `s3:PutObject`, `s3:ListBucket`
- `dynamodb:PutItem`, `dynamodb:DescribeTable`
- `sns:Publish`
- `logs:*` (for debugging)

---

## 🙋‍♀️ Author
Made by Bita – Cloud & Data Engineer
