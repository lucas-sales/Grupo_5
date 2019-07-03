CREATE SCHEMA PostoDeCombustivel;
USE PostoDeCombustivel;

CREATE TABLE Regiao(
cod_regiao INTEGER NOT NULL AUTO_INCREMENT,
logradouro VARCHAR(50),
numero INTEGER,
complemento VARCHAR(30),
bairro VARCHAR(20),
cidade VARCHAR(20),
estado CHAR(2),
pais VARCHAR(20),
PRIMARY KEY (cod_regiao)
);

CREATE TABLE Bandeira(
nome_bandeira VARCHAR(10) NOT NULL,
url VARCHAR(20),
PRIMARY KEY (nome_bandeira)
);

CREATE TABLE Posto(
cnpj_posto VARCHAR(14) NOT NULL,
cod_regiao INTEGER,
nome_bandeira VARCHAR(10),
razao_social VARCHAR(30),
nome_fantasia VARCHAR(30),
telefone VARCHAR(10),
PRIMARY KEY (cnpj_posto),
FOREIGN KEY (cod_regiao) REFERENCES Regiao(cod_regiao) ON DELETE SET NULL,
FOREIGN KEY (nome_bandeira) REFERENCES Bandeira(nome_bandeira) ON DELETE SET NULL
);

CREATE TABLE Funcionario(
matricula VARCHAR(30) NOT NULL,
nome VARCHAR(40),
data_nascimento DATE,
cpf VARCHAR(11) NOT NULL,
PRIMARY KEY (matricula)
);

CREATE TABLE Cliente(
cod_cliente INTEGER NOT NULL AUTO_INCREMENT,
nome VARCHAR(40),
tipo VARCHAR(3),
PRIMARY KEY (cod_cliente)
);

CREATE TABLE PessoaJuridica(
cod_cliente INTEGER NOT NULL,
razao_social VARCHAR(30),
cnpj VARCHAR(14) NOT NULL,
tipo_organizacao VARCHAR(10),
PRIMARY KEY (cod_cliente),
FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente)
);

CREATE TABLE PessoaFisica(
cod_cliente INTEGER NOT NULL,
cpf VARCHAR(11) NOT NULL,
rg VARCHAR(7),
data_nascimento DATE,
PRIMARY KEY (cod_cliente),
FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente)
);

CREATE TABLE Veiculo(
placa VARCHAR(7) NOT NULL,
cod_cliente INTEGER,
marca VARCHAR(20),
modelo VARCHAR(20),
ano VARCHAR(4),
PRIMARY KEY (placa),
FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente) ON UPDATE CASCADE
);

CREATE TABLE Abastecimento(
cod_operacao INTEGER NOT NULL AUTO_INCREMENT,
cnpj_posto VARCHAR(14),
matricula VARCHAR(10),
placa VARCHAR(7),
data_hora DATETIME NOT NULL,
PRIMARY KEY (cod_operacao),
FOREIGN KEY (cnpj_posto) REFERENCES Posto(cnpj_posto),
FOREIGN KEY (matricula) REFERENCES Funcionario(matricula),
FOREIGN KEY (placa) REFERENCES Veiculo(placa) ON UPDATE CASCADE
);

CREATE TABLE TipoCombustivel(
id_combustivel INTEGER NOT NULL AUTO_INCREMENT,
nome VARCHAR(20),
preco DOUBLE,
PRIMARY KEY (id_combustivel)
);

CREATE TABLE AbastecimentoCombustivel(
momento DATETIME,
cod_operacao INTEGER NOT NULL AUTO_INCREMENT,
id_combustivel INTEGER,
preco DOUBLE NOT NULL,
PRIMARY KEY (momento),
FOREIGN KEY (cod_operacao) REFERENCES Abastecimento(cod_operacao) ON UPDATE CASCADE,
FOREIGN KEY (id_combustivel) REFERENCES TipoCombustivel(id_combustivel) ON UPDATE CASCADE
);