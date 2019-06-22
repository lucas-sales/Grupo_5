CREATE SCHEMA `teste_projeto`:
USE `teste_projeto`;

CREATE TABLE `teste_projeto`.`funcionario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `dataNascimento` DATE NULL,
  `email` VARCHAR(60) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `teste_projeto`.`Regiao` (
    `cod_regiao` INT NOT NULL AUTO_INCREMENT,
    `logradouro` VARCHAR(12),
    `numero` VARCHAR(12),
    `complemento` VARCHAR(12),
    `bairro` VARCHAR(12),
    `cidade` VARCHAR(12),
    `estado` VARCHAR(12),
    `pais` VARCHAR(12),
    PRIMARY KEY (`cod_regiao`));

CREATE TABLE `teste_projeto`.`bandeira`(
    nome_bandeira VARCHAR(32) NOT NULL,
    url,
    PRIMARY KEY (`nome_bandeira`));

CREATE TABLE `teste_projeto`.`posto`(
    cnpj_posto VARCHAR(12),
    razao_social VARCHAR(12),
    nome_fantasia VARCHAR(12),
    telefone VARCHAR(12),
    PRIMARY KEY(`cnpj_posto`));

ALTER TABLE `posto` ADD CONSTRAINT `fk_cod_regiao` FOREIGN KEY ( `cod_regiao` ) REFERENCES `Regiao` ( `cod_regiao` );
ALTER TABLE `posto` ADD CONSTRAINT `fk_nome_bandeira` FOREIGN KEY ( `nome_bandeira` ) REFERENCES `bandeira` ( `nome_bandeira` );

INSERT INTO `teste_projeto`.`funcionario` (`nome`, `dataNascimento`, `email`) VALUES
('João José', '1988-12-12', 'joao_jose@gmail.com'),
('Maria João', '1998-07-06', 'maria.joao@hotmail.com'),
('Luis Augusto', '1999-01-01', 'luisaugusto123@gmail.com'),
('Lilian da Luz', '1960-06-06', 'lilian43@gmail.com');