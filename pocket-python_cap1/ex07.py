num = input("Insira dois números inteiros: ")

num1, num2 = map(int, num.split())
if num1 != num2:
    if (num1 > num2) :
        print(f"Os números inseridos em ordem crescente são: {num2}, {num1}")
    else:
        print(f"Os números inseridos em ordem crescente são: {num1}, {num2}")
else: 
    print("Os números digitados são iguais!!")