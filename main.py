n = 0
a = 0
b = 0
c = 0
vb = 0
while n == 0:
    e = int(input(
        "Em qual representante você deseja votar? 1- Ana, 2- Bruno, 3- Carlos ou 4- Voto em branco. Se já votou você deseja 5- Consultar resultado parcial ou 6-Encerrar votação?"))
    if e == 1:
        print("Você votou em Ana!")
        a += 1
    elif e == 2:
        print("Você votou em Bruno!")
        b += 1
    elif e == 3:
        print("Você votou em Carlos!")
        c += 1
    elif e == 4:
        print("Voto branco confirmado!")
        vb += 1
    elif e == 5:
        print("")
    elif e == 6:
        print("")
    else:
        print("Essa opção não existe! Tente novamente.")
print(f" Votos de Ana: {a}")
print(f"Votos de Bruno: {b} ")
print(f"Votos de Carlos: {c}")
print(f"Votos em branco: {vb}")
