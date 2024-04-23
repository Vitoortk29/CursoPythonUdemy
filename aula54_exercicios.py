''' Exercicio 1

    informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro. '''


numero = (input(f'\nDigite um Número inteiro: '))

if numero.isdigit():
    numero_int = int(numero)
    par = numero_int % 2 == 0
    par_texto = 'impar'

    if par:
        par_texto = 'par'

    print(f'\n O Número {numero_int} é {par_texto}')
else:
    print(f'\nVocê não digitou um número inteiro')


#   OUTRA FORMA DE RESOLVER O EXERCICIO 1                                                                                 


numero = (input(f'\nDigite um Número inteiro: '))


try:
    numero_int = int(numero)
    par = numero_int % 2 == 0
    par_texto = 'impar'

    if par:
        par_texto = 'par'

    print(f'\n O Número {numero_int} é {par_texto}')
except:
    print(f'\nVocê não digitou um número inteiro')


#----------------------------------------------------------------------------------------------------------------------------------

''' Exercicio 2

    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.'''


hora =  int(input('\nDigite um horario: '))

if hora >= 0 and hora <= 11:
    print('\nBom dia !')

elif hora >= 12 and hora <= 17:
    print('\nBoa Tarde !')

elif hora >= 18 and hora <= 23:
    print('\nBoa Noite !')

else:
    print('\nNão conheço essa hora !')

#   OUTRA FORMA DE RESOLVER O EXERCICIO 2                                                                                 


hora =  int(input('\nDigite um horario: '))

try:
    if hora >= 0 and hora <= 11:
        print('\nBom dia !')

    elif hora >= 12 and hora <= 17:
        print('\nBoa Tarde !')

    elif hora >= 18 and hora <= 23:
        print('\nBoa Noite !')

    else:
        print('\nNão conheço essa hora !')
        
except:
    print('Digite apenas Números Inteiros !')

#----------------------------------------------------------------------------------------------------------------------------------

# Exercicio 3

''' Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". '''


nome_primeiro = input('\nDigite seu primeiro Nome: ')
tamanho = len(nome_primeiro)

if tamanho > 1:   # Está linha uso para obrigar o usuaria a digitar um Número maior que 1
    if tamanho <= 4:
        print('\nSeu Nome é Curto !\n')
    elif tamanho >= 5 and tamanho <= 6:
        print('\nSeu Nome é Normal !\n')
    else:
        print('\nSeu Nome é muito grande !\n')
else:    # Esta linha usamos para gerar o erro se o usuario digitar um número abaixo de 1 entra nesse else e exibe a mensagem abaixo
    print('Digite mais de uma Letra !') 