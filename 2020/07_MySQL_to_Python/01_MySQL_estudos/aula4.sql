#Apagar database
#drop database cadastro;

#Criar um novo banco de dados, mas agora
#não iremos usar ";" para colocar 2 constrants
create database cadastro
default character set utf8
default collate utf8_general_ci;#Fechar com ;

use cadastro;

create table pessoas (
id int NOT NULL AUTO_INCREMENT,#Auto_increment -> ele coloca índices dec acordo com o preenchimento
nome varchar(30) NOT NULL,# Não aceita ficar sem valor
nascimento date,
sexo enum('M','F'), # Só aceita M ou F
peso decimal(5,2), # dá 5 espaços e 2 casas abaixo da vírgula, ex: 103.45
altura decimal(3,2),
nacionalidade varchar(20) DEFAULT 'Brasil', #Constrant Default
PRIMARY KEY (id) # Não pode ter CPF repetido
)DEFAULT CHARSET = utf8;
