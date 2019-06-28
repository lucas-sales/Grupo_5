import pymysql.cursors

#connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='EAPD3PE42pe**&&',
                            db='postodecombustivel',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)