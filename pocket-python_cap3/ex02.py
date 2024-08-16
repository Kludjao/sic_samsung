def is_palindrome(s):
    s = ''.join(s.split()).lower()

    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    
    return False

string = input("Digite uma palavra para a verificação se é um palindromo: ")

if is_palindrome(string):
    print(f'"{string}" é um palíndromo.')
else:
    print(f'"{string}" não é um palíndromo.')