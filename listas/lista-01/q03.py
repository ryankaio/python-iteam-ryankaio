# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (26/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

nome_completo = input("Digite seu nome completo: ")
cpf = str(input("Digite seu CPF (somente números): "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura (em metros): "))
try:
    idade_em_2026 = 2026 - ano_nascimento
    print(f"Idade em 2026: {idade_em_2026} anos")
except ValueError:
    print("Erro: o ano de nascimento deve ser um número inteiro.")
print(f" Olá {nome_completo}, seu cpf é {cpf}, você tem {idade_em_2026} anos e tem {altura} metros de altura.")

# A altura é representada por um número decimal, pois as pessoas podem ter alturas que não são inteiras (por exemplo, 1.75 metros). Usar um tipo int para altura não seria adequado, pois não permitiria representar essas medidas com precisão.