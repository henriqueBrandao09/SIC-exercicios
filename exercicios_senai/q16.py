a = int(input("Digite dois valores inteiro:"))
b = int(input("Digite dois valores inteiro:"))
if a % b==0:
    print(f"{a} é múltiplo de {b}")
elif  b % a==0:
    print(f"{b} é múltiplo de {a}")
else:
    print("Não são múltiplos")
