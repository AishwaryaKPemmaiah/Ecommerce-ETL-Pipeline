'''from pyspark.sql import SparkSession
from config.spark_config import get_spark_session
from src.data_cleaning import clean_data
from src.data_transformation import enrich_orders

def load_json(spark, filepath):
    return spark.read.json(filepath)

def run_etl():
    spark = get_spark_session()

    customers_df = load_json(spark, "data/customers.json")
    products_df = load_json(spark, "data/products.json")
    orders_df = load_json(spark, "data/orders.json")
    transactions_df = load_json(spark, "data/transactions.json")

    customers_df = clean_data(customers_df)
    orders_df = enrich_orders(orders_df, transactions_df)

    customers_df.show()
    products_df.show()
    orders_df.show()
    transactions_df.show()

if __name__ == "__main__":
    run_etl()


    '''
'''
from pyspark.sql import SparkSession
from delta import DeltaTable
from config.spark_config import get_spark_session
from src.data_cleaning import clean_data
from src.data_transformation import enrich_orders

# GCS Delta Table Path
GCS_PATH = "gs://your-bucket-name/delta_tables/"

def load_json(spark, filepath):
    return spark.read.json(filepath)

def write_to_delta(df, table_name):
    """Writes DataFrame to Delta format on GCS"""
    delta_path = f"{GCS_PATH}{table_name}"
    df.write.format("delta").mode("overwrite").save(delta_path)
    print(f"Data written to Delta: {delta_path}")

def run_etl():
    spark = get_spark_session()

    # Extract: Load JSON Data
    customers_df = load_json(spark, "data/customers.json")
    products_df = load_json(spark, "data/products.json")
    orders_df = load_json(spark, "data/orders.json")
    transactions_df = load_json(spark, "data/transactions.json")

    # Transform: Clean and Enrich Data
    customers_df = clean_data(customers_df)
    orders_df = enrich_orders(orders_df, transactions_df)

    # Load: Write to Delta Tables
    write_to_delta(customers_df, "customers")
    write_to_delta(products_df, "products")
    write_to_delta(orders_df, "orders")
    write_to_delta(transactions_df, "transactions")

    print("ETL Process Completed Successfully!")

if __name__ == "__main__":
    run_etl()
'''
from config.spark_config import get_spark_session
from src.data_ingestion import load_json
from src.data_cleaning import clean_data
from src.data_transformation import enrich_orders
from src.data_loader import write_to_delta

def run_etl():
    spark = get_spark_session()

    # Extract: Load JSON Data
    customers_df = load_json(spark, "data/customers.json")
    products_df = load_json(spark, "data/products.json")
    orders_df = load_json(spark, "data/orders.json")
    transactions_df = load_json(spark, "data/transactions.json")

    # Transform: Clean and Enrich Data
    customers_df = clean_data(customers_df)
    orders_df = enrich_orders(orders_df, transactions_df)

    # Load: Write to Delta Tables
    write_to_delta(customers_df, "customers")
    write_to_delta(products_df, "products")
    write_to_delta(orders_df, "orders")
    write_to_delta(transactions_df, "transactions")

    print("ETL Process Completed Successfully!")

if __name__ == "__main__":
    run_etl()
