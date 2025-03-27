from pyspark.sql.functions import col, lower

def clean_data(df):
    return df.withColumn("email", lower(col("email")))
