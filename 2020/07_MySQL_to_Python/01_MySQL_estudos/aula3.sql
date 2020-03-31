#Aula 3 MySQL Curso em Vídeo
create database cadastro;

#Acessar banco de dados
use cadastro; # Vai ficar em negrito 'cadastro' no canto esquerdo, ou seja, você acessou

create table pessoas (
nome varchar(30), # Var + char (constante)
idade tinyint(3),#economiza mais bits do que int
sexo char(1), #Char apenas caracteres
altura float,
nacionalidade varchar(20)
);

#descreva
describe pessoas;

#obs: varchar < char ... mais leve, em banco de dados
#precisamos pensar sempre no 'peso'