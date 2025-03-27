from pyspark.sql import SparkSession
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
