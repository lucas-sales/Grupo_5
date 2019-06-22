CREATE SCHEMA `teste_projeto` ;
USE `teste_projeto`;

CREATE TABLE `teste_projeto`.`funcionario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `dataNascimento` DATE NULL,
  `email` VARCHAR(60) NULL,
  PRIMARY KEY (`id`));

INSERT INTO `teste_projeto`.`funcionario` (`nome`, `dataNascimento`, `email`) VALUES
('João José', '1988-12-12', 'joao_jose@gmail.com'),
('Maria João', '1998-07-06', 'maria.joao@hotmail.com'),
('Luis Augusto', '1999-01-01', 'luisaugusto123@gmail.com'),
('Lilian da Luz', '1960-06-06', 'lilian43@gmail.com');