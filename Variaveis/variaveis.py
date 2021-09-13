# Para declarar uma variável em Python é muito simples
# Diferente da maioria de outras linguagens não é necessário declarar o tipo da variável

a = 2
b = 'Oi'
c = 2.13
d = True # ou False

x = ()
y = []
z = {}

# O Python ele identifica qual o tipo da variável como podemos ver no print a seguir
# A função type() é usada para podermos saber qual o tipo da variável

print(f'O tipo de a é: {type(a)} \n')
print(f'O tipo de b é: {type(b)} \n')
print(f'O tipo de c é: {type(c)} \n')
print(f'O tipo de d é: {type(d)} \n')
print(f'O tipo de x é: {type(x)} \n')
print(f'O tipo de y é: {type(y)} \n')
print(f'O tipo de z é: {type(z)} \n')

# Estes são os principais tipos de variáriveis dentro de Python
# inteiros, strings, floats, boolean, tuplas, listas e dicionários
# semelhante a outras linguagens

# BONUS
'''
Caso queria mudar o tipo da variável basta voce usar
uma mascara de tipo para que o Python a converta
Observe a seguir:
'''
num = 10
print(f'O tipo de num antes de mudar é {type(num)}')

num = str(num) # mudando o tipo da variável numa

print(f'O tipo de de num agr é: {type(num)}')
