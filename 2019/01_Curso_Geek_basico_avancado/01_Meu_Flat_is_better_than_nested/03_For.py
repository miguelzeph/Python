# Com For.
old_list = [2, 4, 7, 5, 13, 16]
new_list = []
for element in old_list:
	if element % 2 == 0:
		new_list.append(element) #Divisão inteira por 2
print(new_list)

# Sem For - COMPREENSÃO DE LISTA "[]" - LIST COMPREHENSIONS
old_list = [2, 4, 7, 5, 13, 16]
new_list = [element for element in old_list if element % 2 == 0]
print(new_list, " Isso é compreensao de lista")

# Perceba que não utilizamos o ":" no final dos FOR e IF.

# Sem For - EXPRESSÃO GERADORA "()" - GENERATORS
old_list = [2, 4, 7, 5, 13, 16]
new_list = (element for element in old_list if element % 2 == 0) # Só alterei aqui ()
print(new_list, " Isso é expressão geradora")