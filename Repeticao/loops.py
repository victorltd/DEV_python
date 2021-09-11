# Exemplo das estruturas de repitções em Python
# Primeiro vamos ver como funciona o FOR 
# Se temos uma Lista de nomes, números e queremos acessar esses valores um por um fazemos o seguinte

nomes = ['Ramon', 'André', 'Leon', 'Victor', 'Matheus']
for i in nomes: # Podemos observar que o valor de saída é o valor que está na lista
    print(i)    # Se fossem números nessa lista funcionaria da mesma maneira imprimindo cada numero da lista

# Para iterar n vezes o for também pode ser da seguinte maneira
print() # Só para pular uma linha
print('Loop For')
n = 10
for j in range(0,n): # OBS: o range em Python vai contar do primeiro valor, nesse caso 0, até n-1, ou seja, de 0 a 9
    print(j)

# Caso queria que o passo do for seja negativo
print() # Só para pular uma linha
print('For incremento negativo')
for k in range(n,1,-1): # Observe que ele começa em 10 e vai até 2
    print(k)

# Para o laço de repetição while temos a condição de parada para que o algoritmo não seja um loop infinito
# Observe a seguir:
print() # Só para pular uma linha
print("Loop While")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Caso precise entrar num loop antes satisfazer uma condição de parada, semelhante um "do while", podemos fazer assim:
print('Outra maneira de usar o While')
cont = 0
while True:
    print(cont)
    cont += 1
    if cont == 10:
        break

