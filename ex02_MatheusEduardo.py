#Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem 
# “ O último número que você digitou foi um [número] " e pare o programa.
i = 0
while i < 5:
    num = int(input('Insira um número: '))
    i = i + 1
print('O último número que você digitou foi', num)

print('Matheus Eduardo Souza')