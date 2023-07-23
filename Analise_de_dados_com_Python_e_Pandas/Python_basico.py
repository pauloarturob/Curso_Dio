# frase = 'Paulo'
# N = 12534
# print(frase[2])
#
# # criando uma lista
#
# animais = [1,2,3]
# print(animais)
#
# animais = ['cão', 'gato', 'passaro']
# print(animais)
# print(animais[0])
#
# #substituir elemento da lista
#
# animais[1] = input('Digite o nome do animal!: ')
# print(animais)
# # remover elemento da lista
#
# animais.remove(input('Digite o animal que deseja retirar da lista: '))
# print(animais)
#
# # contanto quantos elementos tem na lista
#
# print(len(animais))
#
# # verificando se o animal esta dentro de uma lista
#
# T = 'papagaio' in animais
# print(T)
#
# # sabendo o numero max/min de uma lista
#
# lista = [500,250,450,1800,654]
# print(max(lista))
# print(min(lista))
#
# #adicionando elemento em uma lista
#
# lista.append(250) # append so aceita um argumento
# print(lista)
#
# lista.extend([55624])
# print(lista)
#
# # verificar quantos valore repetidos tem dentro de uma lista
#
# contar_repetidos = lista.count(input("Digite valor desejado: "))
# print(contar_repetidos)
#
# # ordenar a lista
#
# ordenar = lista.sort()
# print(ordenar)

# -----------------------------------------------------------------------------
# Dicionarios
# Criando um dicionario
dc = {"Maça":15, "pera":55, "uva":45}
print(dc)

# Acessando velores do dicionario
A = dc["Maça"]
print(A)

# Modificar valor do um chave da lista
B = dc["Maça"] = 38
print(B)

# Retornar todas as chaves do dicionario
C = dc.keys()
print(C)

# Retornando valores do dicionario
D = dc.values()
print(D)

# Verificando se já exite uma chave no dicionario e caso não exista inserir
E = dc.setdefault("Limão",63)
print(E)
print(dc)