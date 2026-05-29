# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q10.py: reescreva a função corrigindo os 3 problemas encontrados.
# 
#   def processar_alunos(alunos=[]):
#       aprovados = []
#       for i in range(len(alunos)):
#           if alunos[i]['nota'] >= 7.0:
#               aprovados = aprovados + [alunos[i]['nome']]
#       print(aprovados)
# 
# Em q10_resposta.txt: identifique cada problema e explique por que é um problema.
# Dica: há um problema em: (1) definição da função, (2) como o loop é escrito, (3) como a lista é construída.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def processar_alunos(alunos=None):
    aprovados = []
    for aluno in alunos:
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome'])
    print(aprovados)