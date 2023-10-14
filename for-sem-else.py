PROIBIDO = ('futebol', 'religião', 'politica')
mensagens = ['religião e futebol', 'hello']

for palavras in mensagens:
    for words in palavras.lower().split():
        if words in PROIBIDO:
            print('texto contem topico indesejado:', words)
            break
    else:
        print('autorizado', palavras)

for palavras in mensagens:
    achou = False
    for words in palavras.lower().split():
        if words in PROIBIDO:
            print('texto contem topico indesejado:', words)
            achou = True
            break
    if not achou:
        print('autorizado', palavras)
