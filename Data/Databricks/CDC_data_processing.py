# 01. Bronze Table ----

# CREATE TABLE bronze_status 
# (user_id INT, status STRING, update_type STRING, processed_timestamp TIMESTAMP);

# INSERT INTO bronze_status
# VALUES  (1, "new", "insert", current_timestamp()),
#         (2, "repeat", "update", current_timestamp()),
#         (3, "at risk", "update", current_timestamp()),
#         (4, "churned", "update", current_timestamp()),
#         (5, null, "delete", current_timestamp())

# 02. Silver Table ------

# CREATE TABLE silver_status (user_id INT, status STRING, updated_timestamp TIMESTAMP)

# UPDATE + INSERT 작업을 모두 수행한 후 silver table 에 MERGE 하기 
def upsert_cdc(microBatchDF, batchID):
    microBatchDF.createTempView("bronze_batch")
    
    query = """
        MERGE INTO silver_status s
        USING bronze_batch b
        ON b.user_id = s.user_id
        WHEN MATCHED AND b.update_type = "update"
          THEN UPDATE SET user_id=b.user_id, status=b.status, updated_timestamp=b.processed_timestamp
        WHEN MATCHED AND b.update_type = "delete"
          THEN DELETE
        WHEN NOT MATCHED AND b.update_type = "update" OR b.update_type = "insert"
          THEN INSERT (user_id, status, updated_timestamp)
          VALUES (b.user_id, b.status, b.processed_timestamp)
    """
    
    microBatchDF._jdf.sparkSession().sql(query)

# upsert_cdc 작업을 Batch 작업으로 수행하기 
def streaming_merge():
    query = (spark.readStream
                  .table("bronze_status")
                  .writeStream
                  .foreachBatch(upsert_cdc)
                  .option("checkpointLocation", f"{DA.paths.checkpoints}/silver_status")
                  .trigger(availableNow=True)
                  .start())
    
    query.awaitTermination() # query 수행 완료까지 대기 


    