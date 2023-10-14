# um print direto tambem mostra a lista NA MESMA LINHA
word = 'hello'
for letras in word:
    print(letras, end='\n')

print('///////')

notas = ['D', 'C', 'B', 'A']
for valor in notas:
    print(valor, end='\n')

for valores, valor in enumerate(notas):
    print((f'{valores *3}', valor))

dias = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
for dia in dias:
    print(f'hoje e {dia}')

for letra in set('hello'):
    print(letra)  # sets são sem ordem

for numero in {5, 4, 3, 2, 1}:
    print(numero)
