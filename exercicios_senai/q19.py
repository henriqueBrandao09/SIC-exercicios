print("-"*50)
print("Bem-vindo a um delicioso restaurante. Aqui está o cardápio.")
print("Hambúrguer(digite H)")
print("Frango(digite F)")
print("Pizza(digite P)")
print("-"*50)
escolha = input("vai querer o que:")
mudar = escolha.upper()
if mudar == "H":
    print("Você escolheu Hambúrguer")
elif mudar == "F":
    print("Você escolheu Frango")
elif mudar == "P":
    print("Você escolheu Pizza")
else:
    print("sua escolha foi incorreta")