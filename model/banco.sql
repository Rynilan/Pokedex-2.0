create database Pokedex;
create table Pokedex.tb_tipos (
	id int (3) not null auto_increment primary key ,
	nome varchar(10) not null
);

create table Pokedex.tb_regioes (
	id int(3) not null auto_increment primary key,
	nome varchar(50) not null,
	offset int(3) not null
);

create table Pokedex.tb_pokemons (
	id int(10) not null auto_increment primary key,
	nome varchar(50) not null,
	tipo_1 int(3) not null,
	tipo_2 int(3),
	foto varchar(100) not null,
	defesa int not null,
	hp int not null,
	ataque int not null,
	regiao int(3) not null,
	descriçao varchar(500),
	foreign key (tipo_2) references tb_tipos(id),
	foreign key (tipo_1) references tb_tipos(id),
	foreign key (regiao) references tb_regioes(id)
);
