num = input("Digite um número inteiro positivo: ")

if num.isdigit():
    num = int(num)

    if num > 0:
        if num % 2 == 0:
            print(f"O número {num} é par!")
        else:
            print(f"O número {num} é ímpar!")
    else:
        print("Entrada digitada inválida. Por favor, digite um número inteiro positivo.")

else:
    print("Entrada digitada inválida. Por favor, digite um número inteiro positivo.")
