import pymysql.cursors

#connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='teste_projeto',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)