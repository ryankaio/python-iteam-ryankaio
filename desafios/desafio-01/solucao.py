# Desafio 01 — Seu Primeiro Script
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
idade = 2026 - ano
hobbies = input('Digite seus hobbies (separados por vírgula): ').split(',')

print(f'Olá, {nome}! Você tem {idade} anos e seus hobbies são: {", ".join(hobbies)}.')

# ── Fim da solução ─────────────────────────────────────────────────────────