
# Só cria se a tabela não existir
create table if not exists cursos (
nome varchar(30) not null unique,# Não deixa colocar 2 cursos c msm nome
descricao text,
carga int unsigned,#unsgined = sem sinal.. isso economiza 1bit pra cada registro
totaulas int,
ano year default '2016'
)default charset = 'utf8';

describe cursos;

alter table cursos
add column idcurso int first;

alter table cursos
add primary key(idcurso);

#apagar coluna
drop table cursos;

create table if not exists teste (id int);

drop table if exists teste;


