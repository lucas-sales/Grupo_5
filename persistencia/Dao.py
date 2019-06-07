import MySQLdb

host = 'localhost'
user = 'root'
password = ''
db = 'Posto_combustivel'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor()

def select(fields, tables, where=None):
    query = 'SELECT' + fields + "FROM" + tables
    if where:
        query = query + "WHERE" + where

    c.execute(query)
    return c.fetchall()