# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

import q06_estatisticas as est


notas = []

print("Digite 10 notas:")

while len(notas) < 10:

    try:
        nota = float(input(f"Nota {len(notas) + 1}: "))

        notas.append(nota)

    except ValueError:
        print("Digite um número válido.")


print("\n===== RESULTADOS =====")

try:
    print(f"Média: {est.media(notas)}")
    print(f"Mediana: {est.mediana(notas)}")
    print(f"Moda: {est.moda(notas)}")
    print(f"Desvio padrão: {est.desvio_padrao(notas)}")

except ValueError as erro:
    print(f"Erro: {erro}")