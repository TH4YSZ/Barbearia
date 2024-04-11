create database Barbearia;
use Barbearia;

create table clientes (
	id int primary key auto_increment,
	nome varchar(255),
    telefone int(9),
    email varchar(255),
    senha varchar(255)
);

INSERT INTO clientes (nome, telefone, email, senha) VALUES
('João Silva', 987654321, 'joao.silva@email.com', '123456'),
('Maria Souza', 987654322, 'maria.souza@email.com', '654321'),
('Pedro Santos', 987654323, 'pedro.santos@email.com', '123123'),
('Ana Oliveira', 987654324, 'ana.oliveira@email.com', '456456'),
('Paulo Costa', 987654325, 'paulo.costa@email.com', '789789');

create table PrecosCortes (
  ID int not null auto_increment,
  TipoCorte varchar (255) not null,
  Preco decimal (10,2) not null,
  primary key (ID)
);

insert into PrecosCortes (TipoCorte, Preco) values
('Corte Masculino', 20.00),
('Corte Feminino', 30.00),
('Corte Infantil', 15.00),
('Escova', 40.00),
('Hidratação', 50.00);

create table Agendamentos (
  ID int not null auto_increment,
  Data date not null,
  Horario time not null,
  Barbeiro varchar (255) not null,
  primary key (ID)
);

insert into Agendamentos (Data, Horario, Barbeiro) values
('2023-03-08', '10:00', 'João'),
('2023-03-08', '11:00', 'Maria'),
('2023-03-08', '12:00', 'Pedro'),
('2023-03-08', '13:00', 'Ana'),
('2023-03-08', '14:00', 'Carlos');

