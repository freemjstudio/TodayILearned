import pymysql # python 과 MYSQL 연동 
import time 

test_db = pymysql.connect(
    user = "test",
    passwd = "test",
    host = "127.0.0.1",
    db = "testdb",
    port = 3306,
    charset = 'utf-8'
)

cursor = test_db.cursor(pymysql.cursors.DictCursor)

# insert data into the member_table 

def insertsql():
    sql_query = """INSERT INTO member_table(NAME, AGE) VALUES (%s, %s)"""
    i = 0
    while i < 100:
        i = i + 1
        cursor.execute(sql_query,('test'))
        test_db.commit()
        time.sleep(1)
    test_db.close() 

if __name__ == "__main__":
    insertsql() 