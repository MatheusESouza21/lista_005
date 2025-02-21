#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
palpite = 0
while palpite < 15 or palpite > 20:
    palpite = int(input('Insira um número entre 15 e 20: '))
    if palpite < 15:
        print('Muito baixo')
    elif palpite > 20:
        print('Muito alto')
print('Obrigado')

print('Matheus Eduardo Souza')

