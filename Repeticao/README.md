Neste topico aprenderemos como funcionam as estruturas de repetição For e While na linguagem python.

Comumente nos deparamos com a necessidade de executar uma instrução repetida vezes, nestas ocasiões utilizamos estruturas de repetição, aqui aprenderemos as estruturas For e While:

FOR - É utilizado quando se precisa executar por uma determinada quantidade de vezes uma ou mais instruções. 
      
      nomes= ['Ramon', 'André', 'Leon', 'Victor', 'Matheus']
      for n in nomes
          print(n)
    
O for percorrerá o vetor nomes, elemento por elemento, e irá atribuir o elemento encontrado à variavel n e printando-a em seguida.
      
WHILE - É utilizado quando se precisa executar uma ou mais instruções enquanto uma ou mais condições estejam sendo atendidas.

      contador = 0
      while contador < 5:
        print(contador)
        contador= contador +1
        
O while executará a instrução(que soma + 1 á variavel contador), enquanto contador atender a condição(ser menor do que 5).

