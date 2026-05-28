# Desafio 04 — Tabuada Personalizada
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (27/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

numero = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")