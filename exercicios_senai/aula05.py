salario = float(input("digite seu salário: "))
aumento = float(input("Quanto aumentou seu sálario em porcentagem: "))
salario_maior = salario + salario * aumento /100
print(f"Salário antigo: R${salario} Salário atual: R${salario_maior}")
