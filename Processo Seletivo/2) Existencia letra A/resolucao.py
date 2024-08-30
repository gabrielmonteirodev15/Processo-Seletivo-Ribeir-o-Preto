palavra = input("Digite uma palavra")

letra = "a"
cont = 0

for char in palavra:
    if char == letra:
        cont += 1

if cont > 0:
    print(f"A letra 'a' foi achada {cont} na palavra {palavra}'")

else:
    print(f"A letra 'a' não foi achada na palavra {palavra}")

