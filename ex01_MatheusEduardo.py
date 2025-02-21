#Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela,
#  quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
num = 0
total = 0
while total <= 50:
    num = int(input('Insira um número: '))
    total = total + num
print('O total é', total)

print('Matheus Eduardo Souza')