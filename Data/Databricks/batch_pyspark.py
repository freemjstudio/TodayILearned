from pyspark.sql.window import Window 

window = Window.partitionBy("alt_id").orderBy(F.col("updated").desc()) # alt_id 기준으로 partion을 나누고 각각은 updated column 내림차순으로 정렬된다. 
# 이 하나의 작업이 batch 작업 ? 
# microBatchDF 라는 파라미터가 어떤 값인지 모르겠음 
def batch_rank_upsert(microBatchDF, batchId):
    (microBatchDF.filter(F.col("update_type").isin(["new", "update"]))
                  .withColumn("rank", F.rank().over(window))
                  .filter("rank == 1")
                  .drop("rank")
                  .createOrReplaceTempView("ranked_updates"))

    microBatchDF._jdf.sparkSession().sql("""
        MERGE INTO users u 
        USING ranked_updates r 
        ON u.alt_id = r.alt_id 
            WHEN MATCHED AND u.updated < r.updated 
              THEN UPDATE SET * 
            WHEN NOT MATCHED 
              THEN INSERT *                                         
    """)