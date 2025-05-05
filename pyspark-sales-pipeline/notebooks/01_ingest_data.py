
# 01_ingest_data.py

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder     .appName("SalesDataIngestion")     .getOrCreate()

# Load data
df = spark.read.csv("s3a://your-bucket-name/sample_sales_data.csv", header=True, inferSchema=True)

# Show data schema
df.printSchema()

# Show first few rows
df.show()
