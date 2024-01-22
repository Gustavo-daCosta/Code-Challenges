p1 = str(input()).split(" ")
p2 = str(input()).split(" ")

valor = ((int(p1[1]) * float(p1[2])) + (int(p2[1]) * float(p2[2])))

print(f"VALOR A PAGAR: R$ {valor:.2f}")
