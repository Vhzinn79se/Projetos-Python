P = (input('Digite algo:')) #o input sempre vai retornar como string

print('o tipo primitivo desse valor é:' ,type(P))
print('só tem espaços?' , P.isspace())
print('é um numero?' , P.isnumeric())
print('é alfabético?', P.isalpha())
print('é alphanumerico?' , P.isalnum())
print('está em maiscula?', P.isupper())
print('está em minusculas' ,P.islower())
print('está capitalizada?', P.istitle())