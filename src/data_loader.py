GCS_PATH = "gs://your-bucket-name/delta_tables/"

def write_to_delta(df, table_name):
    """Writes DataFrame to Delta format on GCS"""
    delta_path = f"{GCS_PATH}{table_name}"
    df.write.format("delta").mode("overwrite").save(delta_path)
    print(f"Data written to Delta: {delta_path}")
