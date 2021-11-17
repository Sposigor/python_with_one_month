questão = input("Você gosta de queijo?[Sim/Não]: ")

positivo = ["Sim", "sim", "s", "S"]
negativo = ["Não", "não", "n", "N"]

if questão.lower() in positivo:
    print("Entendi")
elif questão.lower() in negativo:
    print("Não entendi")
else:
    print('Quem?')