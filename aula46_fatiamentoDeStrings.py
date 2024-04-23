"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

#Exemplos
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[1:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[3])  #Neste caso eu peguei o espaço por isso no terminal não apresentou nada(O espaço é considerado como caracter)
print(variavel[0:9:4])   # Neste caso adicionamos o passo que significa de quanto em quantos caracteres que ele vai pular
print(len(variavel))    # A função len mostra a quantidade de caracteres da strings
