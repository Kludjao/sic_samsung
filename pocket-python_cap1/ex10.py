def armstrong(num):
    string_num = str(num)
    soma_cubo = 0
    for nume in string_num:
        soma_cubo += int(nume) ** 3
    return soma_cubo == num

numero_armstrong = []
for num in range(100, 1000):
    if armstrong(num):
        numero_armstrong.append(num)

print(f"Números Armstrong de três dígitos: {numero_armstrong}")
