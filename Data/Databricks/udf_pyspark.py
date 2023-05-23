def load_user_lookup():
    query = (spark.readStream
                  .table("registered_users")
                  .selectExpr("salted_hash(user_id) AS alt_id", "device_id", "mac_address", "user_id")
                  .writeStream
                  .option("checkpointLocation", f"{DA.paths.checkpoints}/user_lookup")
                  .trigger(availableNow=True)
                  .table("user_lookup")
                  )
    query.awaitTermination()