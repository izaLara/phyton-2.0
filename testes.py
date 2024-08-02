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

# compras4 = ['leite', 'couve', 'tomate']
# compras5 = ['sal', 'arroz', 'ovos']
# compras = compras4 + compras5
# print(compras)

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


# import NumPy as np


# def is_valid(sudoku, x, y, value):
#     return value not in sudoku[x, :] and value not in sudoku[:, y] and value not in quadrant(sudoku, x, y)


# def quadrant(sudoku, x, y):
#     xx = x // 3
#     yy = y // 3
#     return sudoku[xx * 3:(xx + 1) * 3, yy * 3:(yy + 1) * 3]


# def possibilities(sudoku, x, y):
#     possibilities = list()
#     for value in range(1, 10):
#         if is_valid(sudoku, x, y, value):
#             possibilities.append(value)
#     return possibilities


# def solver(sudoku, solutions):
#     for (x, y), value in np.ndenumerate(sudoku):
#         if value == 0:
#             for possibility in possibilities(sudoku, x, y):
#                 sudoku[x, y] = possibility
#                 solver(sudoku, solutions)
#                 sudoku[x, y] = 0
#             return
#     solutions.append(sudoku.copy())


# if __name__ == '__main__':
#     sudoku = np.array([5, 3, 0, 0, 7, 0, 0, 0, 0,
#                        6, 0, 0, 1, 9, 5, 0, 0, 0,
#                        0, 9, 8, 0, 0, 0, 0, 6, 0,
#                        8, 0, 0, 0, 6, 0, 0, 0, 3,
#                        4, 0, 0, 8, 0, 3, 0, 0, 1,
#                        7, 0, 0, 0, 2, 0, 0, 0, 6,
#                        0, 6, 0, 0, 0, 0, 2, 8, 0,
#                        0, 0, 0, 4, 1, 9, 0, 0, 5,
#                        0, 0, 0, 0, 8, 0, 0, 7, 9]).reshape([9, 9])
#     solutions = list()
#     solver(sudoku, solutions)
#     for solution in solutions:
#         print(solution)


# def quadrante(num_alt,sudoku):
    
#     sudoku=[3, 3, 0, 0, 7, 0, 0, 0, 0,
#         6, 0, 0, 1, 9, 5, 0, 0, 0,
#         0, 9, 8, 0, 0, 0, 0, 6, 0,
#         8, 0, 0, 0, 6, 0, 0, 0, 3,
#         4, 0, 0, 8, 0, 3, 0, 0, 1,
#         7, 0, 0, 0, 2, 0, 0, 0, 6,
#         0, 6, 0, 0, 0, 0, 2, 8, 0,
#         0, 0, 0, 4, 1, 9, 0, 0, 5,
#         0, 0, 0, 0, 8, 0, 0, 7, 9]


# alteracao = input (" ")

# print(alteracao)

# minha_lista2 = [2,3,4],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5],[3,4,5]

# for item in minha_lista2:
#    print(item)

# produtos = [
#     {'id': '2810', 'tipo': 'forno', 'ano': 2020},
#     {'id': '9812', 'tipo': 'celular', 'ano': 2019},
#     {'id': '7756', 'tipo': 'geladeira', 'ano': 2022}
# ]

# print(produtos)
# ###

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [0, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [0, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# def jogo (numeros , alteracao):
#     numeros = sudoku[0][3]  
#     alteracao = input("Digite um número: ")

#     for numero in sudoku:
#         print(alteracao)

#     if numero == numeros:
#             print("erro")
#             return numeros
# print(jogo)
    


# lista6 = ['um', 2, 3.14, [10, 20, 30]]
# lista6[3] = 4 # Seleciona o elemento, e o da um novo valor
# print(lista6)


# sudoku = [[1,2,3,0,0,0,0,0,4,
#            2,3,4,5,6,7,0,0,0,
#            7,8,5,3,0,1,0,1,0],
#            [5,7,6,1,0,0,0,4,0,
#            4,0,0,0,4,0,0,0,0]]

# def contagens(sudoku): # uma função chamada contagens - 
#   lista = {}  # Dicionario -- se encontra vazio

#   for numero in sudoku: # se palavra estiver na minha_lista, executa o código:
      
#     if numero not in lista: 
#         print(sudoku[1][0]) # Se palavra não estiver no dicionario, o valor será 0

#         lista[numero] = 0# Será incrementado mais um número
#         return lista  # chama a função
  
# print(contagens(sudoku))


# sudoku = [1,2,3,0,0,0,0,0,4,
#            2,3,4,5,6,7,0,0,0,
#            7,8,5,3,0,1,0,1,0,
#            5,7,6,1,0,0,0,4,0,
#            4,0,0,0,4,0,0,0,0]

# def jogo(sudoku):
#     numeros = {}

#     for numero in sudoku:

#         if numero not in numeros:
#            numeros[numero] == 0


#         return numeros


# print(jogo(sudoku))




# import pygame
# pygame()
# Janela = pygame.display.set_mode (( 500 , 500 ))
# pygame. display.set_caption ( "JOGO SUDOKU por DataFlair" )
# x = 0
# z = 0
# diferença = 500 / 9
# valor = 0
# grid_padrão = [
#         [ 0 , 0 , 4 , 0 , 6 , 0 , 0 , 0 , 5 ] ,
#         [ 7 , 8 , 0 , 4 , 0 , 0 , 0 , 2 , 0 ] ,
#         [ 0 , 0 , 2 , 6 , 0 , 1 , 0 , 7 , 8 ] ,
#         [ 6 , 1 , 0 , 0 , 7 , 5 , 0 , 0 , 9 ] ,
#         [ 0 , 0 , 7 , 5 , 4 , 0 , 0 , 6 , 1 ] ,
#         [ 0 , 0 , 1 , 7 , 5 , 0 , 9 , 3 , 0 ] ,
#         [ 0 , 7 , 0 , 3 , 0 , 0 , 0 , 1 , 0 ] ,
#         [ 0 , 4 , 0 , 2 , 0 , 6 , 0 , 0 , 7 ] ,
#         [ 0 , 2 , 0 , 0 , 0 , 7 , 4 , 0 , 0 ] ,
#     ]
 
 
# fonte = pygame.fonte.SysFont( "comicsans" , 40 )
# font1 = pygame.fonte.SysFont( "comicsans" , 20 )

# def cordão ( pos ) : 

#     global x
#     x = pos [ 0 ] //diferença
#     z global z
#     z = pos [ 1 ] //diferença
 
# def destaquebox () : 
#     for k in range ( 2 ) : 
#         pygame ( Janela , ( 0,0,0 ) , ( x * diff- 3 , ( z +k ) * diff ) , ( x * diff +diff+ 3 , ( z + k ) * diff ) , 7 )
#         pygame ( Janela , ( 0,0,0 ) , ( ( x+k ) * diferença ,z * diferença ) , ( ( x +k ) * diferença,z * diferença + diferença ) , 7 )   