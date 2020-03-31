# DDL x DML...
#DDL = data definition language
#ex: CREATE DATABASE...CREATE TABLE...alter

#DML = data manipulation language
#ex: insert into



#abrir banco de dados ( OU CLICAR 2X NO BANCO DE DADOS AO LADO)
#use cadastro;

#Podemos deixar de inserir no início o 'id'.. pq ele
# tem uma constrants que gera automático na ordem
insert into pessoas
(id,nome,nascimento,sexo,peso,altura,nacionalidade)
values
('1','Godofredo','1984-01-02','M','78.5','1.83','Brasil');

select * from pessoas;

# vou fazer sem o ID, note que ele preenche automaticamente
insert into pessoas
(nome,nascimento,sexo,peso,altura,nacionalidade)
values
('Priscila','1995-01-02','M','51.5','1.63','Brasil');


select nome,id from pessoas;

#Podemos colocar como Default...
insert into pessoas
(id,nome,nascimento,sexo,peso,altura,nacionalidade)
values
(DEFAULT,'Priscila','1995-01-02','M','51.5','1.63',default);


# Se for inserir dados e a ordem das colunas não for alterada, não precisa colocar 
#(id,nome.....) ... pois ele já entende a sequência
#ex:
insert into pessoas values
(DEFAULT,'Miguel','1990-10-03','M','76.5','1.79',default);


#inserir vários dados ao msm tempo
insert into pessoas values
(DEFAULT,'Junior','1998-10-03','M','75.5','1.70',default),
(DEFAULT,'Fernando','2000-10-03','M','88.5','1.90',default),
(DEFAULT,'Gui','1993-12-08','M','80','1.79',default),
(DEFAULT,'Ana','1965-10-03','F','70.5','1.74',default);
