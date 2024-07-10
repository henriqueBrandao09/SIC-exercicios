# Programa para imprimir a tabela de multiplicação de 1 a 9 usando while

# Inicializa o multiplicador
multiplicador = 1

# Loop externo para cada número da tabela de multiplicação
while multiplicador <= 9:
    print(f"Tabela de multiplicação do {multiplicador}:")
    
    # Inicializa o multiplicando
    multiplicando = 1
    
    # Loop interno para imprimir as multiplicações para o multiplicador atual
    while multiplicando <= 10:
        resultado = multiplicador * multiplicando
        print(f"{multiplicador} x {multiplicando} = {resultado}")
        multiplicando += 1
    
    # Incrementa o multiplicador para passar para o próximo número
    multiplicador += 1
    print()  # Adiciona uma linha em branco entre as tabelas de multiplicação


