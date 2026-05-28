# Desafio 03 — Sistema de Multas
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print("Multado! Você excedeu o limite de 80km/h")
    
    multa = (velocidade - 80) * 7
    
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Boa viagem! Dirija com segurança")