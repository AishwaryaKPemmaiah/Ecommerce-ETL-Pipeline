from pyspark.sql import SparkSession

def load_json(spark: SparkSession, filepath: str):
    """Loads JSON data into a Spark DataFrame"""
    return spark.read.json(filepath)
