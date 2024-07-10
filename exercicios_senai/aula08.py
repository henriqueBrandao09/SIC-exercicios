deposito = float(input("Qual valor vai ser depositado:"))
juros = float(input("Qual é taxa de juros em porcentagem:"))
rendimento = deposito * juros / 100
valor_total = deposito + rendimento
print(f"O rendimento foi de R$ {rendimento:.2f}")
print(f"O valor total após o rendimento é de R$ {valor_total:.2f}")