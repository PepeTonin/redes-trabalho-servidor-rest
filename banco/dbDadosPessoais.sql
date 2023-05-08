create database dadosPessoais;
use dadosPessoais;

create table nomes(
	id int not null auto_increment,
    nome varchar(100) not null,
    primary key (id)
);

create table telefones(
	id int not null auto_increment,
    idNome int not null,
    constraint FK_idNomes_in_telefones foreign key (idNome) references nomes(id),
    telefone varchar(20) not null,
    primary key (id)
);

create table enderecos(
	id int not null auto_increment,
    idNome int not null,
    constraint FK_idNomes_in_enderecos foreign key (idNome) references nomes(id),
    estado varchar(100) not null,
    cidade varchar(100) not null,
    bairro varchar(100) not null,
    rua varchar(100) not null,
    numero int not null,
    primary key (id)
);