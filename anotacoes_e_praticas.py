# FUNÇÕES
# Para a utilização das funções são definidos parâmetros e em ssguida um valor para eles

def calcular_pagamento(qtd_horas, valor_hora):  # é criada uma funçaõ que contem os parâmetros de quantidadade de horas e o valor pelas horas
  horas = float(qtd_horas) # aqui os valores que serão inseridos pelo input serão convertidos para float
  taxa = float(valor_hora)
  if horas <= 40:   # Se a quantidade de horas inseridas forem menores que 40 , executarão o código abaixo:
    salario=horas*taxa
  else:
    h_excd = horas - 40  # Se elas forem menores que 40, será executado o código abaixo:
    salario = 40*taxa+(h_excd*(1.5*taxa)) #  a taxa é multiplicada por 1.5
  return salario  # será retornada o resultado da função

# ACIMA FOI DEFINIDO O QUE ACONTECE NA FUNÇÃO

str_horas= input('Digite as horas: ')
str_taxa=input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('O valor de seus rendimentos é R$',total_salario)

# ACIMA FOI CRIADO O CÓDIGO PARA EXIBIÇÃO NO CONSOLE
 
 ###

peso = float(input('Digite seu peso: ')) # O usuario insere seus dados
altura = float(input("Digite sua altura: "))

def calculo_imc(peso, altura): # a função é definida com seus parâmetros
    print(peso / altura ** 2)

calculo_imc(75, 1.68) # a funçõa é chamada

#LISTAS

lista = [1,2,3,4] # esta é uma lista simples
lista2 = ["zero", 1,2,3,4[1,2,3]] # esta lista contém uma lista com uma string e outra lista dentro

lista3 = ('Python') # aqui foi criada uma variavel
nova_lista = list (lista3) # a função lista pega o item da variavel e o transforma em lista, mesmo que a principio não seja uma
print (lista3)  # aqui o valor é printado desta forma:
['P', 'y', 't', 'h', 'o', 'n'],

#
lista4 = ['um', 2, 3.14]
print(lista4 [0])
print(lista4 [1])
print(lista4 [2])

#
lista = [1,2,3,4] # esta é uma lista simples
lista2 = ["zero", 1,2,3,4[1,2,3]] # esta lista contém uma lista com uma string e outra lista dentro
#
lista3 = ('Python') # aqui foi crada uma variavel
nova_lista = list (lista3) # a função lista pega o item da variavel e o transforma em lista, mesmo que a principio não seja uma
print (lista3)
#
#Para acessar a lista que esta dentro da lista
lista5 = ['um', 2, 3.14, [10, 20, 30]]
print(lista5 [3]) # printará o terceiro elemento da variavel (no caso, a segunda lista)
print(lista5 [3][0]) # printará o terceiro elemento da lista (que é outra lista), e depois o elemento dessa lista 

#
# PARA MODIFICAR UM ELEMENTO DA LISTA
lista6 = ['um', 2, 3.14, [10, 20, 30]]
lista6[3] = 4 # Seleciona o elemento, e o da um novo valor
print(lista6)

lista6[1:] = ['dois', 'tres', 'quatro'] # inteiros podem ser convertidos para string
print(lista6)


#

#Para adicionar elementos na lista
compras = ['leite', 'couve', 'tomate']
compras.append('frango') # é adicionada com a função append
print(compras)

compras2 = ['leite', 'couve', 'tomate']
compras2.insert(1, 'queijo') # aqui é definida a posição em que o novo elemento é adicionado
print(compras2)
['leite', 'queijo', 'couve', 'tomate']

compras3 = ['leite', 'couve', 'tomate']
compras3.extend(['sal', 'arroz', 'ovos'])
print(compras3)  # Aqui será adicionada um NOVO elemento ao PRIMEIRO elemento

compras4 = ['leite', 'couve', 'tomate']
compras5 = ['sal', 'arroz', 'ovos']
compras = compras4 + compras5
print(compras) # Aqui duas variaveis estão sendo CONCATENADAS


# O método COUNT conta o numero de vezes que o item ou substring especificado ocorre no alvo. O método funciona de forma semelhante com string e listas
minha_string = "Quantas madeiras um esquilo empilharia se pudesse empilhar madeira"
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

# DICIONARIO -- CONCEITO E CARACTERISTICAS

#Os itens são adicionados por key (uma chave), e cada key representa um valor(value) - os valores podem ser acessados e alterados através da uma key

meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["banani"] = "banana"
meu_dicionario["cembalo"] = "cravo"
print(meu_dicionario)
print(meu_dicionario["apina"])

palavra = input("Por favor, digite uma palavra: ") #assim que uma palavra do dicionario for adicionada, aparecerá a tradução
if palavra in meu_dicionario:
    print("Tradução: ", meu_dicionario[palavra])
else:   
    print("Palavra não encontrada")

#ou -- looping

for chave in meu_dicionario:  # for faz repetir o que esta dentro da chave meu_dicionario quantas vezes for necessarias(como um looping)
    print("chave", chave)  # chave = os itens no meu_dicionarioa
    print("valor",meu_dicionario[chave]) # o que for escrito no input será buscado na chave


# O dicionario pode conter strings com valores inteiros

resultados = {}
resultados["Marry"] = 4
resultados["Alice"] = 5
resultados["Larry"] = 2

lists = {}
lists[5] = [1,2,3]
lists[42] = [5,4,5,4,5]
lists[100] = [5,2,3]

#

lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"]

def contagens(minha_lista1): # uma funçõa chamada contagens - 
  palavras = {}  # Dicionario -- se encontra vazio

  for palavra in minha_lista1: # se palavra estiver na minha_lista, executa o código:
      
    if palavra not in palavras: 
        palavras[palavra] = 0 # Se palavra não estiver no dicionario, o valor será 0

        palavras[palavra] += 1 # Será incrementado mais um número
        return palavras  # chama a função
  
print(contagens(lista_palavras))