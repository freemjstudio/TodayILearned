from pyspark.sql import functions as F

# update from bronze to silver streaming data 
def update_silver():
    query = (spark.readStream
                  .table("bronze")
                  .withColumn("processed_time", F.current_timestamp())
                  .writeStream.option("checkpointLocation", f"{DA.paths.checkpoints}/silver")
                  .trigger(availableNow=True)
                  .table("silver"))
    
    query.awaitTermination()

# update Key-Value Aggregates (ex. sum, mean, count ...)

def update_key_value():
    query = (spark.readStream # read the streaming data 
                  .table("silver")
                  .groupBy("id")
                  .agg(F.sum("value").alias("total_value"), # aggregate data 
                       F.mean("value").alias("avg_value"),
                       F.count("value").alias("record_count"))
                  .writeStream # write the stream to the new table 
                  .option("checkpointLocation", f"{DA.paths.checkpoints}/key_value")
                  .outputMode("complete")
                  .trigger(availableNow=True)
                  .table("key_value"))
    
    query.awaitTermination()
    