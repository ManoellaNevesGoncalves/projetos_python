import re

def valida(cnpj):
    cnpj = apenas_numeros(cnpj)
    print(cnpj)

def apenas_numeros(cnpj):
     return re.sub(r'[^0-9]', '', 'cnpj')