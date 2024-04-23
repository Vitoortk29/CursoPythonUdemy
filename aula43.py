# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'

print('á' in nome)  #Resultado é True
print('z' in nome)  #Resultado é False
print('vio' in nome)  #Resultado é True
print('zero' in nome)  #Resultado é False

#OBS: O operador in faz uma pergunta se está no caso acima ele está perguntando se a letra ou sequencia de letra declarada contém na variavel.

print('vio' not in nome)  #Resultado é False
print('zero' not in nome)  #Resultado é True

#OBS: O operador in not inverte a pergunta como no exemplo a cima que ele pergunra se a sequencia de letra não contém na váriavel.


#Exemplo de aplicação do operador in

nome= input('Digite seu Nome: ')
encontrar= input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')