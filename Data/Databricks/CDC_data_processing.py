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