# def calcular_pagamento(qtd_horas, valor_hora):  # é criada uma funçaõ que contem os parâmetros de quantidadade de horas e o valor pelas horas
#   horas = float(qtd_horas) # aqui os valores que serão inseridos pelo input serão convertidos para float
#   taxa = float(valor_hora)
#   if horas <= 40:   # Se a quantidade de horas inseridas forem menores que 40 , executarão o código abaixo:
#     salario=horas*taxa
#   else:
#     h_excd = horas - 40  # Se elas forem menores que 40, será executado o código abaixo:
#     salario = 40*taxa+(h_excd*(1.5*taxa)) #  a taxa é multiplicada por 1.5
#   return salario  # será retornada o resultado da função

# str_horas= input('Digite as horas: ')
# str_taxa=input('Digite a taxa: ')
# total_salario = calcular_pagamento(str_horas,str_taxa)
# print('O valor de seus rendimentos é R$',total_salario)

###

# peso = float(input('Digite seu peso: '))
# altura = float(input("Digite sua altura: "))

# def calculo_imc(peso, altura):
#     print(peso / altura ** 2)

# calculo_imc(75, 1.68)

###

# lista = [1,2,3,4]
# lista2 = ["zero", 1,2,3,4[1,2,3]]

# lista3 = ('Python')
# nova_lista = list (lista3)
# print (lista3)

#

# lista4 = ['um', 2, 3.14]
# print(lista4 [0])
# print(lista4 [1])
# print(lista4 [2])

#

# lista5 = ['um', 2, 3.14, [10, 20, 30]]
# print(lista5 [3])
# print(lista5 [3][0])

#

# compras = ['leite', 'couve', 'tomate']
# compras.append('frango')
# print(compras)
# ['leite', 'couve', 'tomate', 'frango']

#

compras4 = ['leite', 'couve', 'tomate']
compras5 = ['sal', 'arroz', 'ovos']
compras = compras4 + compras5
print(compras)

###

# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["banani"] = "banana"
# meu_dicionario["cembalo"] = "cravo"
# print(meu_dicionario)
# print(meu_dicionario["apina"])

# palavra = input("Por favor, digite uma palavra: ")
# if palavra in meu_dicionario:
#     print("Tradução: ", meu_dicionario[palavra])
# else:
#     print("Palavra não encontrada")

#

# resultados = {}
# resultados["Marry"] = 4
# resultados["Alice"] = 5
# resultados["Larry"] = 2

# lists = {}
# lists[5] = [1,2,3]
# lists[42] = [5,4,5,4,5]
# lists[100] = [5,2,3]



#

# lista_palavras = [
#   "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#   "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#   "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
# ]

# def contagens(minha_lista1): 
#   palavras = {} 

#   for palavra in minha_lista1: 
#     if palavra not in palavras: 
#         palavras[palavra] = 0 

#         palavras[palavra] += 1 
#         return palavras
  
# print(contagens(lista_palavras))