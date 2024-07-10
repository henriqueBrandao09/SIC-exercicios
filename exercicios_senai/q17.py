print("Escolha uma operação")
print("adição = 1")
print("subtração = 2")
print("multiplicaçaõ = 3")
print("Divisão = 4")
n = int(input("Qual operação vai escolher:"))
if n==1:
    number = float(input("Digite uma número:")) 
    number1 = float(input("Digite uma número:"))
    op ="+"
    result = number + number1
    print(f"{number} {op} {number1}= {result}")
elif n==2:
    number = float(input("Digite uma número:"))
    number1 = float(input("Digite uma número:"))
    op ="-"
    result = number - number1
    print(f"{number} {op} {number1}= {result}")
elif n==3:
    number = float(input("Digite uma número:"))
    number1 = float(input("Digite uma número:"))
    op ="*"
    result = number * number1
    print(f"{number} {op} {number1}= {result}")
elif n==4:
    number = float(input("Digite uma número:"))
    number1 = float(input("Digite uma número:"))
    op ="/"
    result = number / number1
    print(f"{number} {op} {number1}= {result}")
else:
    print("número incorreto para operação") 
