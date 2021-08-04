from random import choice

a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4] #[] representa lista

escolhido = choice(lista) #rando.choice escolhe de forma aleatoria oque esta dentro da lista

print('O aluno escolhido para apagar o quadro é o(a):{}'.format(escolhido))