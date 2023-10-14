estoque = {'produto': 'caixa de canetas', 'preco': 10.00,
           'novo': False, 'sobrando': 500}

for nome in estoque:
    print(nome)  # imprime somente os nomes chaves .keys()

for preco in estoque.values():
    print(preco)  # imprime somente os valores .values()

for nome, preco in estoque.items():
    print(nome, '=', preco)  # imprime a variavel inteira .items()
