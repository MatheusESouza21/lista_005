#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.
numeros = []
num = int(input('Digite um número (0 para sair): '))
numeros.append(num)
while num != 0:
    num = int(input('Digite um número (0 para sair): '))
    if num in numeros:
        print('Esse número já foi digitado.')
        numeros.append(num)
        i = numeros.index(num)
        numeros.pop(i)
    else:
       numeros.append(num)
print(numeros)

print('Matheus Eduardo Souza')

