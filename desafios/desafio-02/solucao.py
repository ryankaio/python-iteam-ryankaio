# Desafio 02 — Calculadora de IMC
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (2026-05-20)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc(peso, altura)
print(f"{nome}, seu IMC é: {imc:.2f}")