from persistencia import db
connection = db.connection

#crud posto
def createPosto(cnpj, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `posto` VALUES (%s, %s, %s, %s, %s, %s);'
            cursor.execute(sql, (cnpj, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone))
        connection.commit()
    finally:
        connection.close()

def selectAllPosto():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `posto`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def selectPostoByCnpj(cnpj):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `posto` WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def updatePosto(cnpj_novo, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone, cnpj_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `posto` SET cnpj_posto=%s, cod_regiao=%s, nome_bandeira=%s, razao_social=%s, nome_fantasia=%s, telefone=%s WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj_novo, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone, cnpj_antigo))
        connection.commit()
    finally:
        connection.close()

def deletePosto(cnpj):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `posto` WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj))
        connection.commit()
    finally:
        connection.close()

#crud bandeira
def createBandeira(nome, url):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `bandeira` VALUES (%s, %s);'
            cursor.execute(sql, (nome, url))
        connection.commit()
    finally:
        connection.close()

def selectAllBandeira():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `bandeira`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def selectBandeiraByNome(nome):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `bandeira` WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def updateBandeira(nome_novo, url, nome_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `bandeira` SET nome_bandeira=%s, url=%s WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome_novo, url, nome_antigo))
        connection.commit()
    finally:
        connection.close()

def deleteBandeira(nome):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `bandeira` WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome))
        connection.commit()
    finally:
        connection.close()


#crud veiculo
def createVeiculo(placa, marca, modelo, ano):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `veiculo` VALUES (%s, %s, %s, %s);'
            cursor.execute(sql, (placa, marca, modelo, ano))
        connection.commit()
    finally:
        connection.close()

def selectAllVeiculo():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `veiculo`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def selectVeiculoByPlaca(placa):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `veiculo` WHERE placa=%s;'
            cursor.execute(sql, (placa))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def updateVeiculo(placa_nova, marca, modelo, ano, placa_antiga):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `veiculo` SET placa=%s, marca=%s, modelo=%s, ano=%s WHERE placa=%s;'
            cursor.execute(sql, (placa_nova, marca, modelo, ano, placa_antiga))
        connection.commit()
    finally:
        connection.close()

def deleteVeiculo(placa):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `veiculo` WHERE placa=%s;'
            cursor.execute(sql, (placa))
        connection.commit()
    finally:
        connection.close()


#crud regiao
def createRegiao(cod_regiao, logradouro, numero, complemento, bairro, cidade, estado, pais):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `regiao` VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            cursor.execute(sql, (cod_regiao, logradouro, numero, complemento, bairro, cidade, estado, pais))
        connection.commit()
    finally:
        connection.close()

def selectAllRegiao():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `regiao`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def selectRegiaoByCod(cod_regiao):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `regiao` WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def updateRegiao(cod_regiao_novo, logradouro, numero, complemento, bairro, cidade, estado, pais, cod_regiao_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `regiao` SET cod_regiao=%s, logradouro=%s, numero=%s, complemento=%s, bairro=%s, cidade=%s, estado=%s, pais=%s WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao_novo, logradouro, numero, complemento, bairro, cidade, estado, pais, cod_regiao_antigo))
        connection.commit()
    finally:
        connection.close()

def deleteRegiao(cod_regiao):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `regiao` WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao))
        connection.commit()
    finally:
        connection.close()

















