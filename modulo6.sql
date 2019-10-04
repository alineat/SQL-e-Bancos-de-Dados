DROP TABLE IF EXISTS Empresas;
DROP TABLE IF EXISTS Funcionarios;
DROP TABLE IF EXISTS Contratos;
DROP TABLE IF EXISTS Contracheques;

CREATE TABLE Empresas
(
id SERIAL PRIMARY KEY,
razao_social VARCHAR(200),
cnpj CHAR(18),
endereco VARCHAR(300)
);

INSERT INTO Empresas (razao_social, cnpj, endereco)
VALUES ('Acme S/A', '12.345.678/0001-99', 'Av. Paulista, 1200');

INSERT INTO Empresas (razao_social, cnpj, endereco)
VALUES ('Tabaraja Ltda', '23.456.789/0001-11', 'Av. Afonso Pena, 1500');

INSERT INTO Empresas (razao_social, cnpj, endereco)
VALUES ('Planeta Diário', '34.567.890/0001-12', 'Av. Alvares Cabral, 330');

SELECT * FROM Empresas;

CREATE TABLE Funcionarios
(
id SERIAL PRIMARY KEY,
nome VARCHAR(100),
cpf VARCHAR(14),
endereco VARCHAR(300)
);

INSERT INTO Funcionarios (nome, cpf, endereco)
VALUES ('Maria Silva', '123.456.789-11', 'Rua Pernambuco, 230');

INSERT INTO Funcionarios (nome, cpf, endereco)
VALUES ('José Santos', '234.567.890-11', 'Rua Espírito Santos, 293');

INSERT INTO Funcionarios (nome, cpf, endereco)
VALUES ('Mauro Antunes', '345.678.901-23', 'Rua Paraíba, 679');

INSERT INTO Funcionarios (nome, cpf, endereco)
VALUES ('Paola Oliveira', '456.789.012-34', 'Rua São Paulo, 69');

SELECT * FROM Funcionarios;

CREATE TABLE Contratos
(
id SERIAL PRIMARY KEY,
data_admissao TIMESTAMP,
salario NUMERIC, 
cargo VARCHAR(100),
id_empresas INT NOT NULL,
id_funcionarios INT NOT NULL
);

INSERT INTO Contratos (data_admissao, salario, cargo, id_empresas, id_funcionarios)
VALUES ('2006-03-01', 1200, 'Secretária', 1, 1);

INSERT INTO Contratos (data_admissao, salario, cargo, id_empresas, id_funcionarios)
VALUES ('2006-05-10', 1700, 'Vigia', 2, 2);

INSERT INTO Contratos (data_admissao, salario, cargo, id_empresas, id_funcionarios)
VALUES ('2006-07-02', 2400, 'Gerente', 1, 3);

INSERT INTO Contratos (data_admissao, salario, cargo, id_empresas, id_funcionarios)
VALUES ('2006-09-15', 2400, 'Office-boy', 1, 9);

SELECT * FROM Contratos;

CREATE TABLE Contracheques
(
id SERIAL PRIMARY KEY,
referencia CHAR(8),
salario NUMERIC,
inss NUMERIC,
irpf NUMERIC,
fgts NUMERIC,
id_contratos INT
);

INSERT INTO Contracheques (referencia, salario, inss, irpf, fgts, id_contratos)
VALUES ('MAR/2016', 1200, 132, 84, 96, 1);

INSERT INTO Contracheques (referencia, salario, inss, irpf, fgts, id_contratos)
VALUES ('ABR/2016', 1200, 132, 84, 96, 1);

SELECT * FROM Contracheques;
