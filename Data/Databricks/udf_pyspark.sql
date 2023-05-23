
CREATE OR REPLACE FUNCTION salted_hash (id STRING) RETURNS STRING 
RETURN sha2(concat(id, "${da.salt}"), 256)