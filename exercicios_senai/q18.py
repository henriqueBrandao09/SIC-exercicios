x = float(input("digite o valor de x:"))
y = float(input("digite o valor de y:"))
if x>0 and y>0:
    print("Primeiro quadrante")
elif x<0 and y>0:
    print("segundo quadrante")
elif x<0 and y<0:
    print("terceiro quadrante")
elif x>0 and y<0:
    print("Quarto quadrante")
    