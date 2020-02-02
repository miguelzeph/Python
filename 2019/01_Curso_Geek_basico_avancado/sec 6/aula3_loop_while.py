#CUIDADO COM OS LOOPING INFINITOS (Crtl + C ou N...não lembro)
#Exemplo do Loop infinito... jogos são assim, estão sempre rodando esperando comandos

x = True
c = 0

while x:

    c = c+1

    print(c)

    if c > 100:

        x = False

# Break = quebra os loops ...
# Pass = passa... continua...
