# O método COUNT conta o npumero de vezes que o item ou substring especificado ocorre no alvo. O método funciona de forma semelhante com string e listas
minha_string = "Quantas madeiraas um esquilo empilharia se pudesse empilhar madeira"
print(minha_string.count("ma"))


# O método REPLACE cria uma nova string, onde uma substring especificada é susbstituida por outra string
minha_string2 = "Oi"
nova_string = minha_string2.replace("Oi","Olá")
print(nova_string)

#MATRIZ --- LISTAS DENTRO DE LISTAS

minha_lista = [[5,2,3],[4,1],[2,2,5,1]] #Encontrar o item na lista que está dentro da outra lista
print(minha_lista)
print(minha_lista [1])
print(minha_lista[1][0])


pessoas = [["Betty", 10, 1.37],["Pedro", 7, 1.25],["Emilly", 32, 1.64],["Alan", 39, 1.78]]
for pessoa in pessoas:  #Colocando os itens da lista pessoas na lista pessoa e buscando o item
    nome = pessoa[0]
    idade = pessoa[1]
    altura = pessoa[2]