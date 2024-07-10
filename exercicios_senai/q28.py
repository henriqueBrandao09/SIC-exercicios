import random as rd
n = None
rando = rd.randint(1,100)
while n!=rando:
    n = int(input("Digite um número: "))
    if n < rando:
        print("Aumente o número")
        print("-----"*10)
    elif n > rando:
        print("diminua o número")
        print("-----"*10)

print(f"O número random correto é : {n}")