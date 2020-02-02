#Aqui eu desenvolvi uma jogada muito útil para meus dados...
for i in range(0,3):
    # Cria variável
    globals()['e%s' % str(i)] = {'real': [], 'imag': []}
    globals()['u%s' % str(i)] = {'real': [], 'imag': []}

    # Adicionar Valores
    for n in range(0,3):
        #Append no vetor
        globals()['e%s' % str(i)]['real'].append(n)
        globals()['e%s' % str(i)]['imag'].append(n)

        globals()['u%s' % str(i)]['real'].append(n)
        globals()['u%s' % str(i)]['imag'].append(n)
print(e0)
print(u0)

print(e1)
print(u1)

print(e2)
print(u2)
