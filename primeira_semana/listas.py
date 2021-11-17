contagem = [1, 2, 3, 4, 5]
coisas_aleatorias = ['oi', 1, 2, 3, 4, 5, 6, 'uhe', 8, 1/2, ['lista', 2, 3, 4]]

for i in contagem:
    print(i)

for i in coisas_aleatorias:
    print(i)

pessoas = []
pessoas.append('Igor')
pessoas.append('Sem teto')
pessoas.append('Uhe')

for i in pessoas:
    print(i)
    
pessoas.remove('Sem teto')

for i in pessoas:
    print(i)
    
animais = ['Leão', 'Zebra', 'Girafa', 'Tigre', 'Crocodilo']
print(animais)
for i in animais:
    print(i)
print(animais[0])
print(animais[1])

print(f'Animais são em {len(animais)}')
print(f'O tipo do animal é {type(animais)}')

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizz')
    elif n % 5 == 0 and n % 3 != 0:
        print('Buzz')