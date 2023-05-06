create database trabalhoRedes;
use trabalhoRedes;

create table agendaContatos(
	id int not null auto_increment,
    nome varchar(100) not null,
    telefone varchar(20) not null,
    primary key (id)
);

select * from agendaContatos;