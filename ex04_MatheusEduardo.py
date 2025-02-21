#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. 
# Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
contagem = 1
nome = input('Qual o nome da pessoa que deseja convidar? ')
print('{} foi adicionado(a) com sucesso no convite!'.format(nome))
confirmacao = input('Você deseja convidar outra pessoa? ')
while confirmacao == 's':
    nome = input('Qual o nome da pessoa que deseja convidar? ')
    contagem = contagem + 1
    print('{} foi adicionado(a) com sucesso no convite!'.format(nome))
    confirmacao = input('Você deseja convidar outra pessoa? ')
print('{} pessoas foram convidadas para a festa.'.format(contagem))

print('Matheus Eduardo Souza')