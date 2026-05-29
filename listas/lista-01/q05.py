# Lista 01 — Questão 05: Encontre o Bug
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# O código abaixo tem um bug lógico — executa sem erros, mas produz resultado errado.
# Copie o código no arquivo, identifique o bug, corrija-o e explique em comentário.
# 
#   def maior_nota(notas):
#       maior = 0
#       for nota in notas:
#           if nota > maior:
#               maior == nota  # bug aqui
#       return maior
#   print(maior_nota([7.5, 9.0, 6.0, 8.5]))

# ── Sua solução abaixo ──────────────────────────────────────────────────────

notas = [7.5, 9.0, 6.0, 8.5]
def maior_nota(notas):
    maior = 0
    for nota in notas:
        if nota > maior:
            maior = nota  # bug aqui
    return maior
print(maior_nota(notas))