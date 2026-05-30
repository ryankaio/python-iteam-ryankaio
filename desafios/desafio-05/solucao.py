# Desafio 05 — Gerenciador de Compras
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# Lista vazia
produtos = []

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    produtos.append(produto)

print("\nLista de produtos:")
for item in produtos:
    print("-", item)

print("Total de itens:", len(produtos))