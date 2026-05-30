# Desafio 07 — Bio-Calculadora
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

from funcoes_mat import area_circulo, volume_esfera, hipotenusa

print("=== MENU DE CÁLCULOS ===")
print("1 - Área do Círculo")
print("2 - Volume da Esfera")
print("3 - Hipotenusa")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    raio = float(input("Digite o raio: "))
    resultado = area_circulo(raio)
    print(f"Área do círculo: {resultado:.2f}")

elif opcao == "2":
    raio = float(input("Digite o raio: "))
    resultado = volume_esfera(raio)
    print(f"Volume da esfera: {resultado:.2f}")

elif opcao == "3":
    cat1 = float(input("Digite o primeiro cateto: "))
    cat2 = float(input("Digite o segundo cateto: "))
    resultado = hipotenusa(cat1, cat2)
    print(f"Hipotenusa: {resultado:.2f}")

else:
    print("Opção inválida!")