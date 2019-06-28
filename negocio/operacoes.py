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
        cursor.close()

def selectAllPosto():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `posto`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectPostoByCnpj(cnpj):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `posto` WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def updatePosto(cnpj_novo, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone, cnpj_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `posto` SET cnpj_posto=%s, cod_regiao=%s, nome_bandeira=%s, razao_social=%s, nome_fantasia=%s, telefone=%s WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj_novo, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone, cnpj_antigo))
        connection.commit()
    finally:
        cursor.close()

def deletePosto(cnpj):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `posto` WHERE cnpj_posto=%s;'
            cursor.execute(sql, (cnpj))
        connection.commit()
    finally:
        cursor.close()

#crud bandeira
def createBandeira(nome, url):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `bandeira` VALUES (%s, %s);'
            cursor.execute(sql, (nome, url))
        connection.commit()
    finally:
        cursor.close()

def selectAllBandeira():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `bandeira`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectBandeiraByNome(nome):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `bandeira` WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def updateBandeira(nome_novo, url, nome_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `bandeira` SET nome_bandeira=%s, url=%s WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome_novo, url, nome_antigo))
        connection.commit()
    finally:
        cursor.close()

def deleteBandeira(nome):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `bandeira` WHERE nome_bandeira=%s;'
            cursor.execute(sql, (nome))
        connection.commit()
    finally:
        cursor.close()


#crud veiculo
def createVeiculo(placa, marca, modelo, ano):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `veiculo` VALUES (%s, %s, %s, %s);'
            cursor.execute(sql, (placa, marca, modelo, ano))
        connection.commit()
    finally:
        cursor.close()

def selectAllVeiculo():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `veiculo`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectVeiculoByPlaca(placa):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `veiculo` WHERE placa=%s;'
            cursor.execute(sql, (placa))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def updateVeiculo(placa_nova, marca, modelo, ano, placa_antiga):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `veiculo` SET placa=%s, marca=%s, modelo=%s, ano=%s WHERE placa=%s;'
            cursor.execute(sql, (placa_nova, marca, modelo, ano, placa_antiga))
        connection.commit()
    finally:
        cursor.close()

def deleteVeiculo(placa):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `veiculo` WHERE placa=%s;'
            cursor.execute(sql, (placa))
        connection.commit()
    finally:
        cursor.close()


#crud regiao
def createRegiao(cod_regiao, logradouro, numero, complemento, bairro, cidade, estado, pais):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `regiao` VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            cursor.execute(sql, (cod_regiao, logradouro, numero, complemento, bairro, cidade, estado, pais))
        connection.commit()
    finally:
        cursor.close()

def selectAllRegiao():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `regiao`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectRegiaoByCod(cod_regiao):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `regiao` WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def updateRegiao(cod_regiao_novo, logradouro, numero, complemento, bairro, cidade, estado, pais, cod_regiao_antigo):
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE `regiao` SET cod_regiao=%s, logradouro=%s, numero=%s, complemento=%s, bairro=%s, cidade=%s, estado=%s, pais=%s WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao_novo, logradouro, numero, complemento, bairro, cidade, estado, pais, cod_regiao_antigo))
        connection.commit()
    finally:
        cursor.close()

def deleteRegiao(cod_regiao):
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM `regiao` WHERE cod_regiao=%s;'
            cursor.execute(sql, (cod_regiao))
        connection.commit()
    finally:
        cursor.close()

#crud funcionario
def createFuncionario(matricula, nome, data_nascimento, cpf):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `funcionario` VALUES (%s, %s, %s, %s);'
            cursor.execute(sql, (matricula, nome, data_nascimento, cpf))
        connection.commit()
    finally:
        cursor.close()

def selectAllFuncionario():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `funcionario`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectFuncionarioByMatricula(matricula):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `funcionario` WHERE matricula=%s;'
            cursor.execute(sql, (matricula))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

#crud cliente
def selectClienteByNome(nome):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `cliente` WHERE nome=%s;'
            cursor.execute(sql, (nome))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectClienteByCpfCnpj(cpfCnpj):
    result = None
    if len(cpfCnpj) == 11:
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM `pessoafisica` WHERE cpf=%s;'
                cursor.execute(sql, (cpfCnpj))
                result = cursor.fetchall()
        finally:
            cursor.close()
    else:
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM `pessoajuridica` WHERE cnpj=%s;'
                cursor.execute(sql, (cpfCnpj))
                result = cursor.fetchall()
        finally:
            cursor.close()
    return result

def createCliente(nome):
    isCliente = selectClienteByNome(nome)
    if not isCliente:
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `cliente(nome)` VALUES (%s);'
                cursor.execute(sql, (nome))
            connection.commit()
        finally:
            cursor.close()
    else:
        return None

def createPessoaJuridica(codCliente, razaoSocial, cnpj, tipoOrganizacao):
    isPessoaJuridica = selectClienteByCpfCnpj(cnpj)
    if not isPessoaJuridica:
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `pessoafisica(cod_cliente, razao_social, cnpj, tipo_organizacao)` VALUES (%s, %s, %s, %s);'
                cursor.execute(sql, (codCliente, razaoSocial, cnpj, tipoOrganizacao))
            connection.commit()
        finally:
            cursor.close()
    else:
        return None

def createPessoaFisica(codCliente, cpf, rg, dataNascimento):
    isPessoaFisica = selectClienteByCpfCnpj(cpf)
    if not isPessoaFisica:
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO `pessoajuridica(cod_cliente, cpf, rg, data_nascimento)` VALUES (%s, %s, %s, %s);'
                cursor.execute(sql, (codCliente, cpf, rg, dataNascimento))
            connection.commit()
        finally:
            cursor.close()
    else:
        return None

def selectAllCliente():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `cliente`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectClienteByCodCliente(codCliente):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `cliente` WHERE cod_cliente=%s;'
            cursor.execute(sql, (codCliente))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

#crud combustivel
def selectAllCombustivel():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `tipocombustivel`;'
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()


def selectCombustivelByNome(nomeCombustivel):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `tipocombustivel` WHERE nome=%s;'
            cursor.execute(sql, (nomeCombustivel))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()

def selectCombustivelById(idCombustivel):
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `tipocombustivel` WHERE id_combustivel=%s;'
            cursor.execute(sql, (idCombustivel))
            result = cursor.fetchall()
            return result
    finally:
        cursor.close()


#crud abastecimento
def getDateTime():
    import time
    timestamp = time.gmtime()
    timestamp_readable = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
    return timestamp_readable

def createAbastecimento(cnpjPosto, matricula, placa):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `Abastecimento(cnpj_posto, matricula, placa, data_hora)` VALUES (%s, %s, %s, %s);'
            cursor.execute(sql, (cnpjPosto, matricula, placa, getDateTime()))
        connection.commit()
    finally:
        cursor.close()

def createAbastecimentoCombustivel(idCombustivel, preco):
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO `AbastecimentoCombustivel(momento, id_combustivel, preco)` VALUES (%s, %s, %s);'
            cursor.execute(sql, (getDateTime(), idCombustivel, preco))
        connection.commit()
    finally:
        cursor.close()

