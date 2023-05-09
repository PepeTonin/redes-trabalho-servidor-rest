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

insert into nomes(nome)
values
	("Pedro Souza"),
	("Dagtiadar Sathalion"),
	("Oseth Irsueth"),
	("Bazbice Cigash"),
	("Balam Grupu");

insert into telefones(idNome, telefone)
values
	(1,"(41) 15694-5526"),
	(1,"(41) 73889-8122"),
	(2,"(48) 44966-4466"),
	(3,"(48) 79659-0521"),
	(4,"(11) 73483-4771"),
    (2,"(11) 70004-4499"),
	(2,"(11) 43466-1715"),
	(3,"(41) 58635-3973"),
	(1,"(61) 60211-0354"),
	(2,"(61) 63749-3338");
    
insert into enderecos(idNome, estado, cidade, bairro, rua, numero)
values
	(1, "PR", "Curitiba", "Centro", "Rua Eduardo Antônio Martins", 586),
    (3, "SC", "Jaragua do Sul", "Jardim Europa", "Rua Alcindo Furlan", 1016),
    (4, "SP", "Anhumas", "Boa Vista", "Rua Gilberto Mestrinho", 951),
    (5, "SC", "Blumenau", "Vorstadta", "Rua Ricardo Luiz Smith", 357),
    (3, "PR", "Maringa", "Zona 06", "Rua Maria Cecília de Lima", 24),
    (5, "SP", "Guarulhos", "Cidade Soinco", "Rua José Maria da Cunha", 07),
    (5, "MS", "Tres Lagoas", "Santos Dumont", "Rua B18", 3524);