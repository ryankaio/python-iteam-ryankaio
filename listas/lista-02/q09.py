# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome

        # Atributos privados
        self.__preco = None
        self.__estoque = estoque

        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):

        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")

        self.__preco = valor


    @property
    def estoque(self):
        return self.__estoque


    def repor(self, qtd):

        if qtd <= 0:
            raise ValueError("A quantidade deve ser positiva.")

        self.__estoque += qtd

    def vender(self, qtd):

        if qtd <= 0:
            raise ValueError("A quantidade deve ser positiva.")

        if qtd > self.__estoque:
            raise ValueError("Estoque insuficiente.")

        self.__estoque -= qtd

    def __str__(self):
        return (
            f"Produto: {self.nome} | "
            f"Preço: R$ {self.__preco:.2f} | "
            f"Estoque: {self.__estoque}"
        )

    def __repr__(self):
        return (
            f"Produto(nome='{self.nome}', "
            f"preco={self.__preco}, "
            f"estoque={self.__estoque})"
        )

produto = Produto("Notebook", 3500.0, 10)

print("=== PRODUTO CRIADO ===")
print(produto)

# Venda
print("\n=== VENDA DE 3 UNIDADES ===")
produto.vender(3)
print(produto)

# Reposição
print("\n=== REPOSIÇÃO DE 5 UNIDADES ===")
produto.repor(5)
print(produto)

# Tentativa de venda além do estoque
print("\n=== TENTATIVA DE VENDA INVÁLIDA ===")

try:
    produto.vender(20)

except ValueError as erro:
    print(f"Erro: {erro}")

# repr()
print("\n=== REPR ===")
print(repr(produto))