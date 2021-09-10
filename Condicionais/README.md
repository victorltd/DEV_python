Aqui na parte de condicionais, iremos tratar sobre o uso de condicionais em python.
Quando se programa, muitas vezes é necessário que determinado bloco de código seja executado apenas se uma determinada condição for verdadeira ou falsa. Em casos assim, pode-se fazer uso de uma estrutura de condição. Aqui trataremos das condições if-else e elif ambas da linguagem Python.
#### If:
O if é uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.
A estrutura do mesmo ocorre com o uso da palavra reservada if, em seguida pela condição que deseja-se analisar, seguido de dois pontos (:), e abaixo daí o que estiver com Indentação (espaço no inicio da linha), será considerado como o código que deve ser executado caso a condição seja verdadeira.
#### Exemplo:
```python
idade = 18
if idade >= 18:
   print('maior de idade')
```
No caso desse código, a variável idade recebeu o número 18, após isso, o if verifica que, caso o valor dentro da variável idade seja maior ou igual a 18, então a mensagem "maior de idade" será entregue ao usuário.

#### If-else:
O if else, vem com a intenção de complementar o uso do if, onde como foi visto, no if caso uma condição seja atendida, uma parcela de código será executada, já com o else, caso aquela condição do if não seja atendida, acontecerá a parcela de código presente no else.
#### Exemplo:
```python
idade = 18
if idade >= 18:
	print('pode beber')
else:
	print('nao pode beber')
```
Nesse caso, se dentro da variável idade existir um número maior ou igual a 18, a mensagem 'pode beber' será impressa, caso contrário, a mensagem 'nao pode beber' será impressa.
#### If-elif-else:
Por fim, em um caso onde é necessário conferir mais de uma condição, utiliza-se o elif, que permite com que varias condições sejam verificadas, e após o uso do mesmo, ainda é possível utilizar o else caso seja necessário.
#### Exemplo:
```python
idade = 18
if idade < 12:
	print('criança')
elif idade < 18:
	print('adolescente')
elif idade < 60:
	print('adulto')
else:
	print('idoso')
```
Nesse código o objetivo é verificar a idade de certa pessoa, e determinar se ele é criança, adolescente, adulto ou idoso, sendo isso feito com base na sua idade, e para isso são feitas 3 verificações se sua idade é menor que 12, menor que 18 ou menor que 60, e cada à cada um é atribuido a impressão da classificação, caso a variável idade correspondá aquela faixa-etária, e caso nenhuma das 3 anteriores funcionem, a mensagem idoso será exibida.

Caso deseje ver esse tutorial em formato de vídeo, segue um link para algo semelhante: https://youtu.be/hSVY5qTD2iE
