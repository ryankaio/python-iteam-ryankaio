# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

notas = []

for i in range(10):

    while True:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota (0 a 10): "))

            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break  
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro: digite um número válido.")

maior_nota = max(notas)
menor_nota = min(notas)

media = sum(notas) / len(notas)

acima_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1

print("\n===== RESULTADOS =====")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade acima da média: {acima_media}")

print("\nClassificação dos alunos:")

for i, nota in enumerate(notas, start=1):

    if nota >= 7.0:
        classificacao = "Aprovado"
    elif nota >= 5.0:
        classificacao = "Recuperação"
    else:
        classificacao = "Reprovado"

    print(f"Aluno {i}: Nota = {nota} -> {classificacao}")