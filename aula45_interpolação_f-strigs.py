"""
Formatação básica de strings
s - corda
d-int
f - flutuar
.<número de dígitos>f
x ou X - Hexadecimal
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ -Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""

variavel= 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}teste')
print(f'{variavel:$^10}.')
print(f'{1000.4873648123746:,.1f}')