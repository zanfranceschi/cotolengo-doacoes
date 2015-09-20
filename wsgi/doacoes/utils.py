

def salvar_foto(conteudo, nome):
    with open(nome, 'wb+') as destino:
        for chunk in conteudo.chunks():
            destino.write(chunk)