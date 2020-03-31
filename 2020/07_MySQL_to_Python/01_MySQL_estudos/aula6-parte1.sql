# Banco de Dados -> Tabelas -> Campos (Colunas)

#Adicionar Coluna no FIMMM (padrão ele coloca no fim)
alter table pessoas
add column profissao varchar(10) not null default 'naosabe';# Se você não colocar not null e default
# ele vai preencher todas as colunas com Null

#desc = describe (podemos usar essas duas formas)
desc pessoas;

# Ver tudo da tabela
select * from pessoas;

#Remover coluna
alter table pessoas
drop column profissao;


#Adicionar Coluna após o nome
alter table pessoas
add column profissao varchar(10) not null default 'naosabe' after nome;

# Para adicionar por primeiro? Não existe a funcao BEFORE...
# então teremos que fazer diferente
alter table pessoas
add column codigo int first;# Não precisa da palavra column

#Redefinir característica das colunas
alter table pessoas
modify column profissao varchar(20) default 'Nao_sabe';

#Modificar o nome da coluna
alter table pessoas
change column profissao prof varchar(20) default 'vazio'; #Observe que você tem que colocar  tipo da variável


# trocar o nome da tabela inteira
alter table pessoas
rename to gafanhotos;

