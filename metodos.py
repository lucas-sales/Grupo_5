import db
connection = db.connection

def createFuncionario(nome, dataNascimento, email):
    with connection.cursor() as cursor:
        sql = 'INSERT INTO `funcionario` VALUES (%s, %s, %s, %s);'
        cursor.execute(sql, ('DEFAULT', nome, dataNascimento, email))
    connection.commit()


def selectAllFuncionarios():
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM `funcionario`;'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result