# Lista 01 — Questão 09: EAFP vs LBYL
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py: reescreva a função abaixo no estilo EAFP usando try/except.
# 
#   def dividir(a, b):
#       if b != 0:
#           return a / b
#       else:
#           return None
# 
# Em q09_resposta.txt: explique o que significa EAFP e qual versão é mais Pythônica.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None