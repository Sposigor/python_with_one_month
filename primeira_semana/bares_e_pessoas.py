# Biblioteca
import random

# Variaveis
bares = ['Bazinho da esquina', 'Barzão do tio', 'Sempre bar', 'Barzinho do tio', 'Apenas um bar']
pessoas = ['Alexia', 'Lorenzo', 'Chris', 'Nutella', 'Samuel', 'Icaro', 'Felipe']

# Aleatoridade das variaveis
random_bares = random.choice(bares)
random_pessoas_1 = random.choice(pessoas)
random_pessoas_2 = random.choice(pessoas)

# Impressão das variaveis
print(f'Você que ir em {random_bares} com {random_pessoas_1} e {random_pessoas_2}')