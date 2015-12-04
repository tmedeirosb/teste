# coding: utf-8

import zipfile

banco = None

# tratando exceção
try:
    banco = zipfile.ZipFile('saida.zip')
except FileNotFoundError:
    print('arquivo não existe')
except PermissionError as pme:
    print('Erro de permissão')
else:
    banco.extractall(path='banco')
finally:
    banco.close()


# definindo classe de exceção
class InvalidDataExeption(Exception):
    pass


# lançando exceção
def validar(kind):
    if not kind in ('a', 'b', 'c'):
        raise InvalidDataExeption('tipo inválido')



try:
    validar('oi')
except Exception as e:
    print('peguei a exceção')
    raise e

