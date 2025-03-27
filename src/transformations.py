from pyspark.sql.functions import col
'''
def enrich_orders(orders_df, transactions_df):
    return orders_df.join(transactions_df, "order_id", "left").select(
        "order_id", "customer_id", "product_id", "amount", "status"
    )

'''
def enrich_orders(orders_df, transactions_df):
    """Enriches orders data by joining with transactions"""
    return orders_df.join(transactions_df, "order_id", "left")
