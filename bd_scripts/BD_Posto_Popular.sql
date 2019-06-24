INSERT INTO Regiao(logradouro, numero, complemento, bairro, cidade, estado, pais) VALUES
('Rua Marionete de Campo Grande', 81, 'Em frente ao supermercado', 'Bairro Amarelo', 'Cidade dos Rios', 'PE', 'Brasil'),
('Rua Perséfone', 103, 'Ao lado da farmácia', 'Bairro Azul', 'Campina Laranja', 'PE', 'Brasil'),
('Avenida dos Três Oitos', 22, 'Perto do hospital', 'Cidade Alta', 'Campina Laranja', 'PE', 'Brasil'),
('Avenida Ramos de Barros', 224, 'Após a prefeitura', 'Cidade Baixa', 'Cidade dos Corais', 'PE', 'Brasil'),
('Rua da Colina', 93, 'Do lado do restaurante', 'Bairro Amarelo', 'Cidade dos Rios', 'PE', 'Brasil');

INSERT INTO Bandeira(nome_bandeira, url) VALUES
('Branca', 'www.postolar.com.br'),
('Shell', 'www.shell.com.br'),
('Petrobras', 'www.petrobras.com.br');

INSERT INTO Posto(cnpj_posto, cod_regiao, nome_bandeira, razao_social, nome_fantasia, telefone) VALUES
('01234567891011', 1, 'Branca', 'Posto Maurício', 'Posto LAR', '32105678'),
('05134567891012', 2, 'Shell', 'Posto Maurício', 'Posto LAR', '32105678'),
('04234567891013', 3, 'Shell', 'Posto Maurício', 'Posto LAR', '32105678'),
('03234567891014', 5, 'Petrobras', 'Posto Maurício', 'Posto LAR', '32105678');

INSERT INTO Funcionario(matricula, nome, data_nascimento, cpf) VALUES
('012', 'Marivaldo José do Maranhão', '1991-03-30', '01234567891'),
('013', 'Arístides Espínola dos Santos', '1990-02-11', '01234567811'),
('014', 'José de Bragança Teixeira', '1981-01-23', '31234567200'),
('015', 'Gabriel Persival Duque da Rocha', '1985-11-02', '21234562831'),
('016', 'Helena Pereira da Silva', '1986-01-22', '11234561021'),
('017', 'Sabrina Pessoa Bulhões', '1978-12-01', '01234567219'),
('018', 'Neusa Liliane da Fonseca Barbosa', '1992-09-08', '01228367891');

INSERT INTO Cliente(nome) VALUES
('Aurélio Brito de Paula'),
('Vanessa dos Santos Cavalcanti'),
('Gabriela Maria Ferreira Pinto'),
('Roberto Carneiro Pessoa'),
('João Paulo Carvalho Nunes'),
('Bruna Fernandes Acioly'),
('Diana Gabrielle Damaceno'),
('Prefeitura da Cidade dos Rios'),
('Hospital Central da Cidade');

INSERT INTO PessoaJuridica(cod_cliente, razao_social, cnpj, tipo_organizacao) VALUES
(8, 'Centro do Governo da Cidade', '01293291910291', 'Pública'),
(9, 'Centro Médico Intensivo', '01293291922211', 'Privado');

INSERT INTO PessoaFisica(cod_cliente, cpf, rg, data_nascimento) VALUES
(1, '12345678910', '1029382', '1988-03-02'),
(2, '22245678910', '1011182', '1989-01-22'),
(3, '33444678910', '1222282', '1990-12-12'),
(4, '12039678910', '1123482', '1981-11-23'),
(5, '01928678910', '1112382', '1980-10-30'),
(6, '12330408111', '2344582', '1995-09-01'),
(7, '12345672938', '1022344', '1996-04-07');

INSERT INTO Veiculo(placa, cod_cliente, marca, modelo, ano) VALUES
('XYZ0901', 1, 'Ford', 'Focus', '2013'),
('XZS2221', 2, 'Chevrolet', 'Equinox', '2019'),
('XWZ4441', 2, 'Ford', 'Ranger', '2017'),
('XWQ1231', 3, 'Fiat', 'Uno', '2001'),
('QWS0121', 4, 'Ferrari', '588', '2019'),
('SSW1101', 5, 'VW', 'Gol', '2002'),
('AWQ0201', 1, 'Honda', 'Civic', '2012');

INSERT INTO Abastecimento(cnpj_posto, matricula, placa, data_hora) VALUES
('03234567891014', '016', 'XZS2221', '2018-09-03 22:01:42'),
('01234567891011', '013', 'XWQ1231', '2018-10-30 10:23:55'),
('01234567891011', '012', 'XYZ0901', '2018-11-03 11:59:21'),
('04234567891013', '017', 'AWQ0201', '2018-11-03 21:20:32'),
('01234567891011', '013', 'XWZ4441', '2018-12-04 08:52:31'),
('05134567891012', '015', 'SSW1101', '2019-01-23 21:44:13'),
('04234567891013', '018', 'SSW1101', '2019-02-03 18:03:41'),
('01234567891011', '013', 'XYZ0901', '2019-03-11 01:11:22'),
('05134567891012', '014', 'XWZ4441', '2019-04-05 03:42:43'),
('01234567891011', '013', 'XYZ0901', '2019-04-12 02:12:04');

INSERT INTO TipoCombustivel(nome) VALUES
('Diesel'),
('Gasolina'),
('Etanol'),
('Gás Natural');

INSERT INTO AbastecimentoCombustivel(momento, cod_operacao, id_combustivel, preco) VALUES
('2018-09-03 22:01:42', 1, 1, 9.88),
('2018-10-30 10:23:55', 2, 2, 11.28),
('2018-11-03 11:59:21', 3, 2, 33.58),
('2018-11-03 21:20:32', 4, 2, 44.11),
('2018-12-04 08:52:31', 5, 3, 19.24),
('2019-01-23 21:44:13', 6, 3, 21.22),
('2019-02-03 18:03:41', 7, 3, 102.29),
('2019-03-11 01:11:22', 8, 1, 11.33),
('2019-04-05 03:42:43', 9, 1, 12.31),
('2019-04-12 02:12:04', 10, 4, 29.37);