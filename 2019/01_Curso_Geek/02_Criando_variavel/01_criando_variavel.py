"Fonte: How do you create different variable names while in a loop?"

for x in range(0,10):

    globals() ['variavel_'+str(x)] = x

print(variavel_8)




