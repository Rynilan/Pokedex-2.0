create database Pokedex;
create table Pokedex.tb_pokemons(
	id int(10) not null auto_increment primary key,
	nome varchar(50) not null,
	descricao varchar(500) not null,
	tipo_1 varchar(10) not null,
	tipo_2 varchar(10),
	forca int(3) not null,
	defesa int(3) not null,
	hp int(3) not null,
	foto varchar(200) not null
);
