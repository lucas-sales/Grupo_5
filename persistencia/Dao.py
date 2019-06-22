import MySQLdb

host = '127.0.0.1'
user = 'root'
password = ''
db = 'Posto_combustivel'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):
    global c

    query = 'SELECT' + fields + "FROM" + tables
    if where:
        query = query + "WHERE" + where

    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):
    global c, con

    query = "INSERT INTO" + table
    if (fields):
        query = query +  "("  + fields + ")"

    query = "VALUES" + ",".join(["(" + v + ")"for v in values])
    print(query)

values = ["DEFAULT, 'Joao Pedro', '2000-01-01', 'Av sao Miguel, 123', 'Recife', 'PE', '12345678911'",
          "DEFAULT, 'Lucas', '1996-01-01', 'Av sao Miguel, 008', 'Recife', 'PE', '12345678913'"]

