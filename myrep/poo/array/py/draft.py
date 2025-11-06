lista = [] # lista vazia
compras = ["carne", "patinho", "pão"] #lista prenchida
print(compras)
# obter o tamanho de uma lista
compras.append("frango") # adicionando elemetos no final
compras.pop()# remover elemnetos no final

compras.insert(0, "farinha") # adiciona um elemento na posição espesifica da lista
compras.pop(0) # removido elemento na posição espesifica da lista 
compras_for = ", ".join(compras)
print(compras_for)


numero = [1,2,3,4,5] 

for i in range(0,3):
    print(compras[i])
