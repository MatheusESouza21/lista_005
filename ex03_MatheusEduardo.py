#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
num1 = int(input('Insira um número: '))
num2 = int(input('Insira mais um número: '))
total = num1 + num2
confirmacao = input('Você deseja adicionar outro número?(S ou N): ').lower()
while confirmacao == 's':
    num = int(input('Digite outro número: '))
    total = total + num
    confirmacao = input('Você deseja adicionar outro número?(S ou N): ')
print('Total:',total)

print('Matheus Eduardo Souza')


