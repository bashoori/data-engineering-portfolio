# 02_transform_data.py

from pyspark.sql.functions import col, to_timestamp, round

# Convert timestamp
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Calculate order total
df = df.withColumn("order_value", round(col("quantity") * col("price"), 2))

# Drop nulls (if any)
df_clean = df.dropna()

# Show transformed data
df_clean.show()
