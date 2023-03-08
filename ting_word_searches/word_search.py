# Requisito 7 - Implemente uma função exists_word
# que verifique a existência de uma palavra em todos
# os arquivos processados
def exists_word(word, instance):
    qtd_vezes = []
    result = []
    for valor in range(len(instance)):
        arquivo = instance.search(valor)
        linhas = arquivo['linhas_do_arquivo']
        for valor in range(len(linhas)):
            if word.lower() in linhas[valor].lower():
                qtd_vezes.append({'linha': valor + 1})

        if len(qtd_vezes) >= 1:
            result.append({
                'palavra': word,
                'arquivo': arquivo['nome_do_arquivo'],
                'ocorrencias': qtd_vezes
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
