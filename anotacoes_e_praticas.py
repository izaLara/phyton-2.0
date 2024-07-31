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

        palavras[palavra] += 1 # Será incrementado u mais um número
        return palavras  # chama a função
  
print(contagens(lista_palavras))