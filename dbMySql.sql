create database trabalhoRedes;
use trabalhoRedes;

create table nomes(
	id int not null auto_increment,
    nome varchar(100) not null,
    primary key (id)
);

create table telefones(
	id int not null auto_increment,
    telefone varchar(20) not null,
    primary key (id)
);

create table nomeTelefone(
	idNome int not null,
    constraint FK_idNome foreign key (idNome) references nomes(id),
    idTelefone int not null,
    constraint FK_idTelefone foreign key (idTelefone) references telefones(id)
);

select * from nomes;