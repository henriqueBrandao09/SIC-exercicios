nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua primeira nota:"))
nota3 = float(input("Digite sua primeira nota:"))

peso1 = int(input("Digite o peso da primeira nota:"))
peso2 = int(input("Digite o peso da primeira nota:"))
peso3 = int(input("Digite o peso da primeira nota:"))

sum = (nota1*peso1) + (nota2*peso2) + (nota3*peso3) 
media = sum / peso1 + peso2 + peso3 
print(f"A média ponderada:{media}")