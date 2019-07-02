import pymysql

def connect_to_db():
    return pymysql.connect(host='localhost',
                           user='your_username',
                           passwd='your_password',
                           db='bookshop',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=False)