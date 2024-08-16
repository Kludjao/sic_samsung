
# def calc_digit(n):
#     def final(digit):
#         return digit**n
#     return final
# num_list = []
# for num in range(1, 6):
#     num_list.append(calc_digit(num))
#     prtin(num_list[num - 1](num))

# 1
# 4
# 27
# 256
# 3125
# Calcule o resultado do código manualmente.


# A função calc_digit(n) retorna final, que é uma função que calcula digit ** n, ou seja, a exponenciação de um número (digit) elevado a n. Quando armazenamos essa função final na lista num_list[], estamos guardando a lógica para calcular a exponenciação para cada valor de n. Agora, seguindo o loop for que vai de 1 a 6 (na real, até 5, porque o range(1, 6) não inclui o 6)

# Praticamente está calculando o numero elavado a ele mesmo

# 1 ** 1 = 1
# 2 ** 2 = 4
# 3 ** 3 = 27
# 4 ** 4 = 256
# 5 ** 5 = 3125