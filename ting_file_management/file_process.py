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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
