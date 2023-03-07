from ting_file_management.file_management import txt_importer
import sys


# Requisito 3 - Implemente a função process no módulo file_process
def process(path_file, instance):
    for valor in range(len(instance)):
        if instance.search(valor)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": (file),
    }
    instance.enqueue(result)
    return sys.stdout.write(str(result))


# Requisito 4 - Implemente uma função remove dentro do
# módulo file_process capaz de remover o primeiro arquivo processado
def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')
    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()

    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


# Requisito 5 - Implemente uma função file_metadata
# dentro do módulo file_process capaz de apresentar
# as informações superficiais de um arquivo processado.
def file_metadata(instance, position):
    try:
        result = instance.search(position)
        return sys.stdout.write(str(result))
    except IndexError:
        return sys.stderr.write('Posição inválida\n')
