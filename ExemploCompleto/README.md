No exemplo do arquivo randomico.py, a intenção é de que você que está passando pelo treinamento possa testar todos os conhecimentos que foram adquiridos durante esse treinamento.

Para que você possa codificar programas complexos, é necessário o conhecimento básico que foram apresentados aqui, e o objetivo é que você possa observar o código e buscar entender onde em cada parte do código são aplicadas as ferramentas que foram estudadas, analisar quais suas funções individuais, e como todas são ligadas juntas para criar um código mais completo.

Além do que já foi ensinado, um último ensinamento seria a utilização de bibliotecas. Grupos de códigos já prontos com funções específicas e feitos por outras pessoas, podem ser utilizados no seu código direto da internet com o acesso a bibliotecas. Para importar um biblioteca para o seu código, basta utilizar a palavra reservada "import", e então o nome da biblioteca, onde para esse exemplo foram utilizadas as bibliotecas "random e time", e da biblioteca time foi utilizada a função sleep que está dentro da biblioteca sleep, e a função choice que está dentro da biblioteca random.

Além disso, é possível dar um apelido para uma biblioteca, visto que muitas possuem nomes bastante grandes, nesse exemplo, damos o apelido de rd para a biblioteca random, com o comando "as" e o apelido em seguida rd.

Durante e realização do código, após declarar as bibliotecas que seriam utilizadas, nas linhas 11, 16 e 25, foram utilizadas as funções:
```python
11  def printbonitinho():

16  def printFormatado(msg):

25  def escolhido(lista):
```
Após isso, foi realizado um print com uma mensagem, então foi feito um while que é um loop, conceito já explicado nesse treinamento, e dentro desse while tem um if, aplicação de condição que também já foi explicado aqui.

Depois, foi utilizada a forma de input, onde é pego através do teclado, uma mensagem, texto, ou número que é digitado pelo usuário. Então uma lista foi criada, com os valores que foram obtidos pelo usuário, e depois foi chamada a função escolhido, que irá escolher aleatoriamente um dos elementos da list:
```python
47  chosen = escolhido(list)
```
Então foi usada a função sleep para demorar alguns segundos antes de continuar o código, após isso foi chamada a função print formatado, seguido da função print bonitinho:
```python
53  printFormatado(chosen)

55  printbonitinho()
```
Que é usada para dar um print bonito, então mais uma vez a função sleep.

Então é chamada a função shuffle que irá mudar a ordem anterior da lista de forma aleatória, e por fim é impressa a nova ordem da lista.
