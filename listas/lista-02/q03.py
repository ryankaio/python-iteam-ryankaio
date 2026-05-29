# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────


def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(produto)


def buscar_por_codigo(inventario, codigo):

    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto

    return None


def listar_abaixo_do_minimo(inventario, minimo):

    produtos_abaixo = []

    for produto in inventario:
        if produto["quantidade"] < minimo:
            produtos_abaixo.append(produto)

    return produtos_abaixo


def valor_total(inventario):

    total = 0

    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]

    return total



inventario = []

adicionar_produto(inventario, "Mouse", "M001", 10, 50.0)
adicionar_produto(inventario, "Teclado", "T001", 3, 120.0)
adicionar_produto(inventario, "Monitor", "MON01", 2, 900.0)
adicionar_produto(inventario, "Cabo USB", "C001", 20, 15.0)

for produto in inventario:
    print(produto)


produto = buscar_por_codigo(inventario, "T001")

if produto:
    print("Produto encontrado:")
    print(produto)
else:
    print("Produto não encontrado.")



baixo_estoque = listar_abaixo_do_minimo(inventario, 5)

for produto in baixo_estoque:
    print(produto)



total = valor_total(inventario)

print(f"Valor total: R$ {total:.2f}")