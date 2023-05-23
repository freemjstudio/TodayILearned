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

update_silver()