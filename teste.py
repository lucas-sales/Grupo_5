import db
from metodos import createFuncionario, selectAllFuncionarios
connection = db.connection



try:
    createFuncionario('gato molhado', '2010-01-01', 'gatomolhado123@gmail.com')
    
    resultadoConsulta = selectAllFuncionarios()
    print(resultadoConsulta)        

finally:
    connection.close()
