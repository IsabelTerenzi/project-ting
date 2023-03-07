import sys


# Requisito 2 - Implemente uma função txt_importer 
# dentro do módulo file_management
def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, 'r') as arquivo:
            result = arquivo.read().split('\n')
            return result
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
