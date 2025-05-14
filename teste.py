def calcular_custo_combustivel(valor_litro, consumo_km_litro, distancia_km):
    return (distancia_km / consumo_km_litro) * valor_litro

def melhor_combustivel(valores_combustiveis, percursos):
    custos = {}

    for nome, preco in valores_combustiveis.items():
        custo_total = 0
        for percurso in percursos:
            distancia, autonomia = percurso
            custo_total += calcular_custo_combustivel(preco, autonomia, distancia)
        custos[nome] = custo_total

    melhor = min(custos, key=custos.get)

    print("\nResultados:")
    for combustivel, custo in custos.items():
        print(f"{combustivel.capitalize()}: R$ {custo:.2f}")

    print(f"\n🏆 Melhor opção: {melhor.capitalize()}")

# Entrada de dados
valores_combustiveis = {
    'gasolina comum': float(input("Digite o valor da gasolina comum (R$): ")),
    'gasolina aditivada': float(input("Digite o valor da gasolina aditivada (R$): ")),
    'etanol': float(input("Digite o valor do etanol (R$): "))
}

percursos = []
while True:
    distancia = float(input("\nDigite a distância do percurso (km): "))
    autonomia = float(input("Digite a autonomia (km/l) estimada para esse percurso: "))
    percursos.append((distancia, autonomia))

    continuar = input("Deseja adicionar outro percurso? (s/n): ").lower()
    if continuar != 's':
        break

# Executa cálculo
melhor_combustivel(valores_combustiveis, percursos)
