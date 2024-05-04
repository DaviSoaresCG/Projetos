create table webuser.tb_intrutores(
	id_instrutor serial,
	nome text NOT NULL,
	sobrenome text NOT NULL,
	data_nascimento date NOT NULL,
	endereco text,
	telefone text NOT NULL,
	
	constraint pk_tb_instrutores primary key(id_instrutor)
);

create table webuser.tb_planos(
	id_plano serial,
	plano text NOT NULL,
	
	constraint pk_planos primary key(id_plano)
);

create table webuser.tb_membros(
	id_membro serial,
	nome varchar(255) NOT NULL,
	sobrenome varchar(255) NOT NULL,
	data_nascimento date NOT NULL,
	endereco text,
	telefone varchar(20),
	email varchar(255),
	cod_tipo_plano integer,
	data_inicio date NOT NULL,
	ativo boolean NOT NULL,
	
	constraint pk_membros_id primary key(id_membro),
	constraint fk_membros_cod_tipo_plano foreign key(cod_tipo_plano) references webuser.tb_planos(id_plano)
);

create table webuser.tb_atividades(
	id_atividade serial,
	nome varchar(255),
	cod_instrutor integer,
	data timestamp NOT NULL,
	duracao int NOT NULL,
	capacidade int NOT NULL,
	cod_tipo_plano int,
	ativo boolean NOT NULL,
	
	constraint pk_atividade_id primary key(id_atividade),
	constraint fk_atividade_cod_tipo_plano foreign key(cod_tipo_plano) references webuser.tb_planos(id_plano) ON DELETE CASCADE
);

create table webuser.tb_agendamentos(
	id_agendamento serial,
	cod_atividade integer,
	cod_membro integer,
	
	constraint pk_agendamentos_id primary key(id_agendamento),
	constraint fk_agendamentos_ativdade foreign key(cod_atividade) references webuser.tb_atividades(id_atividade) ON DELETE CASCADE,
	constraint fk_agendamentos_membro foreign key(cod_membro) references webuser.tb_membros(id_membro) ON DELETE CASCADE
);

