'''
Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar,
à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste em vários casos de teste. A primeira linha de entrada contém um inteiro N que indica
a quantidade de casos de teste. Cada caso de teste consiste em dois valores A e B maiores que zero,
cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor,
confome exemplo abaixo.
'''
#
N = int(input())

while (N > 0):
    A, B = input().split(" ")
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")
    N -= 1

