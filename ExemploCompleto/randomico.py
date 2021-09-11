# Antes de começarmos o código vamos importar bibliotecas que vão nos axiliar para realizar o exemplo
import random as rd # Observe que nessa linha temos 'as rd' a palavra reservada 'as' irá dar um apelido para a biblioteca importada
from time import sleep
from random import choice

''' 
Caso ao rodar o programa você não tenha uma das bibliotecas você deve usar o comando "pip install <nome da biblioteca>" 
exemplos: pip install random
          pip install time
'''
def printbonitinho():
    print("="*40)
    print("  Mudando a ordem da lista digitada")
    print("="*40)

def printFormatado(msg):
    tamanho = len(msg) + 4
    print("O Sorteado da vez foi...")
    sleep(3)
    print("="*tamanho)
    print(f"  {msg}")
    print("="*tamanho)
    print()

def escolhido(lista):
    chosen = choice(lista) # Usando a biblioteca para que ela, aleatoriamente, selecione um valor da lista
    return chosen

print("Número aleatório de 1 a 10:")
while True: # Loop até que a biblioteca gere um número menor ou igual a 10
    num = rd.randint(1,21)
    sleep(1) # Para o código por 1 segundo
    if num <= 10:
        print(f" {num}")
        break
print()
# Nessa parte, durante a execução do algoritmo iremos digitar 5 nomes para embaralharmos eles dentro de uma lista
print('Agora voce vai digitar uma lista com 5 nomes')
p1=str(input("Digite o nome do primeiro: "))
p2=str(input('Digite o nome do segundo: '))
p3=str(input("Digite o nome do terceiro: "))
p4=str(input('Digite o nome do quarto: '))
p5=str(input('Digite o nome do quinto: '))

list=[p1,p2,p3,p4,p5] # Lista com os valores obtidos do usuário

chosen = escolhido(list) # Chamada da função que irá escolher um dos nomes da lista

print()
print('Sorteando um nome da lista temos...')
sleep(5)
print()
printFormatado(chosen) # Chamada da função para ter um print formatado

printbonitinho() # Chamada da nossa função para um print bonito
print()
sleep(5) # Para dar um suspense para nova ordem da lista

rd.shuffle(list) # Muda a ordem anterior da lista, ou seja, deixa a ordem toda aleatória
# A seguir é printada a lista com a nova ordem
print('Nova ordem da lista')
print("O primeiro da ordem agora é: "+ list[0])
print("O segundo da ordem agora é: "+ list[1])
print("O terceiro da ordem agora é: "+ list[2])
print("O quarto da ordem agora é: "+ list[3])
print("O quinto da ordem agora é: "+ list[4])
print()
