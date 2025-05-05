# Real-Time Sales Analytics Pipeline with PySpark, AWS, and Databricks

## 📌 Project Overview
This project demonstrates how to build a scalable data pipeline using PySpark in Databricks to process and analyze e-commerce sales data stored in AWS S3. The pipeline computes real-time KPIs such as revenue, top-selling products, and average cart size.

## 🛠 Tools Used
- PySpark
- Databricks (Community Edition)
- AWS S3 (Free Tier)
- Delta Lake
- GitHub

## 🧱 Architecture

![ETL Diagram](etl_diagram.png)

## 🗃 Folder Structure

```
/pyspark-sales-pipeline/
├── notebooks/
│   ├── 01_ingest_data.py
│   ├── 02_transform_data.py
│   ├── 03_generate_kpis.py
├── data/
│   └── sample_sales_data.csv
├── docs/
│   └── etl_diagram.png
├── README.md
```

## ✅ Features
- Load raw CSV data from S3
- Transform using PySpark (cleaning, aggregations, calculations)
- Write output to Delta Lake
- Save final KPIs for dashboard use

## 📊 Sample KPIs
- Total Revenue (Daily)
- Top 5 Products by Quantity Sold
- Average Cart Size
- Revenue by Product Category

## 🚀 How to Run
1. Upload `sample_sales_data.csv` to your S3 bucket
2. Open Databricks Community Edition
3. Use the provided notebooks to process and analyze the data
4. View results and exported KPI datasets

## 🙋‍♀️ Author
Bita Ashoori – Data Engineer
