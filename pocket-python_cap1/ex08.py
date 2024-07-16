idade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não): "))

estcv = int(input("Você é casado(a)? (digite 1 se sim, 0 se não): "))

if idade >= 0 and idade <= 1 and estcv >= 0 and estcv <= 1:
    
    if idade == 1 and estcv == 0:
        print("Você é maior de idade e solteiro.")
    elif idade == 1 and estcv == 1:
        print("Você é maior de idade e casado.")
    elif idade == 0 and estcv == 0:
        print("Você não é maior de idade e é solteiro.")
    else:
        print("Você não é maior de idade e é casado.")
else:
    print("Entrada digitada inválida!")     