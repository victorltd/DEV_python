# Código exemplo de funções

def hello(meu_nome):
  print('Olá, ' + meu_nome +'\n')# Obs: quando é colocado o '+' para o python ele vai cocatenar as strings

def hello2(meu_nome,idade):
   return f'\nOlá, {meu_nome}\nVoce tem {idade} anos'

# ATENÇÃO: Nensse código será necessária sua interação. Digite o que for requirido quando você executar o código

hello(input('Hello 1, Digite seu nome:\n')) # O input irá receber o valor que o usuário digitar quando o código for executado

retorno = hello2(input('Hello 2, Digite seu nome:\n'), int(input('Agora sua idade:\n')))
print(retorno)