#Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, 
#diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
adivinha = 50
tentativas = 0
palpite = 0
while palpite != adivinha:
    palpite = int(input('Insira um número: '))
    tentativas = tentativas + 1
    if palpite < adivinha:
        print('Muito baixo')
    elif palpite > adivinha:
        print('Muito alto')
print('Parabéns! Você acertou o número em {} tentativas!'.format(tentativas))

print('Matheus Eduardo Souza')
