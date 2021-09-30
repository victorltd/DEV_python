
Para criar uma variável em Python, tudo o que você precisa fazer é especificar o nome da variável e, em seguida, atribuir um valor a ela.

Variáveis são utilizadas para **armazenar valores em memória**, elas permitem gravar e ler esses dados com facilidade a partir do nome a ela atribuido.
O Python usa o sinal de igual ‘=’ para atribuir valores a variáveis.
Variáveis pode ser criadas em qualquer linha em branco no código.

Normas para declarar variáveis: 
   1. Nomes de variáveis em Python podem começar com uma letra ou um underline:
      - Ex: x 
      - Ex: _x
  - O restante do nome da variável pode ter letras, números e underline.
      - Ex: x_y 
      - Ex: x123
  - Os nomes de variáveis são sensíveis a maiúsculas, ou seja, x é diferente de X.
  
  - Não pode usar palavras reservadas do python como nome de variável válido. Lista de palavras reservadas do Python: ‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘async’,  ‘await’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’

Tipos de veriáveis: inteiros, reais, strings, booleans, listas, tuplas e dicionários. O tipo de variável é definido de acordo com o valor que lhe é atribuido.

  - Inteiros: 
    1. São as variáveis quem podem armazenar valores inteiros. 
       - Ex: x = 10 (foi atribuido um valor 10 para a variável x, logo x agora vale 10)
    
  - Reais: 
    1. São as variáveis quem podem armazenar valores reais(numeros decimais). O ponto '.' é utilizado para separar a parte inteira da decimal
       - Ex: _45x = 1.1 (foi atribuido um valor 1.1 para a variável x, logo x agora vale 1.1)
 
  - String: 
    1. São as variáveis que armazenam caracteres. É necessário que a cadeia de caracteres esteja entre aspas simples ou duplas.
       - Ex: xh65_ = "Engenharia de Software III" 
       - Ex: y = 'Engenharia de Software III'
    
  - Booleans: 
    1. São variáveis que armazenam um valor lógico, True ou False.
       - Ex: x = True 
       - Ex: y = False
  
  - Listas: 
    1. Para criar uma lista são usados os símbolos de [] (colchetes)
       - Ex: lista1 = []
    3. Uma lista em python é uma **estrutura de dados** composta por itens organizados de forma linear e são separados pela vírgula.
       - Ex: lista2 = [1, 2, 3, 4, 5]
    5. Os podem ser acessado a partir de um índice, que representa sua posição na coleção (iniciando em zero). 
       - Ex: lista2[1] (acessando o número 2)
    7. Os itens de uma lista podem ser de tipos variados (incuindo outras listas). 
       - Ex: lista3 = [1, 1.1, 'Juazeiro', true, [1,2,3], 2]
    9. Quando um indice negativo é passado, a lista é lida de trás para frente. 
       - Ex: lista3[-3] (acessando o boolean true)
    11. Possuem tamanho variável(crescem automaticamente a medida que objetos são inseridos).
    12. Os valores de cada índice podem ser alterados.
        - Ex: lista3[0] = 1.45 (em lista3, remove o inteiro 1 e coloca o real 1.45)
    
  - Tuplas: Semelhantes a uma lista, porém
    1. Para criar uma tupla são usados os símbolos de ()(parenteses).
    	- Ex: tupla = (1, 2, 3)
    2. São listas, porém **imutáveis**. 
    	- Ex: tupla[1] = 4 (é levantado um erro 'Raises Error')
    3. Os itens de uma tupla podem ser acessados a partir de um indice.
    	- Ex: tupla[1] (acessando o número 2)
  
  - Dicionários:
    1. Para criar um dicionário são utilizados os símbolos de {} (chaves);
    	- Ex: dic = {}
    2. Dicionários podem ser vistos como uma coleção de pares chave:valor;
    	- Ex: dic = {'nome': joao, 'idade': 23} (nome e idade são as chave, joao e 23 são os valores
    3. As chaves em um dicionário precisam ser únicas, porém os valores não precisam
    	- Ex: dic2 = {'nome': pedro, 'nome': carlos} (erro)
    5. Dicionários são endereçados por chave, não por posição;
    	- Ex: dic['nome'] (acessando o valor 'joao')
    6. Tem tamanho variável e podem conter objetos de qualquer tipo, inclusive ouros dicionários;
    	- Ex: dic['sexo'] = 'M' (adiciona o campo 'sexo' ao dicionário e atribui 'M' a esse campo) 
    7. São mutáveis como as listas;
    8. Atribuir um valor a uma nova chave adiciona uma nova entrada ao dicionário;
	
    
 
    
    
