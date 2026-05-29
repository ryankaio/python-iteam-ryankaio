# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (Ryan Kaio Sena da Silva)
# Data:  (29/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):

    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        return self.salario * 0.05


# Lista com objetos de diferentes tipos
funcionarios = [
    Funcionario("Ana", 3000),
    Gerente("Carlos", 8000, "TI"),
    Estagiario("Marina", 1500, "Engenharia")
]


# Iterando e exibindo bônus
for funcionario in funcionarios:

    bonus = funcionario.calcular_bonus()

    print(f"Nome: {funcionario.nome}")
    print(f"Bônus: R$ {bonus:.2f}")
    print("-" * 30)


"""Explicação:
O Python chama automaticamente a versão correta de calcular_bonus() 
por causa do POLIMORFISMO.

Mesmo percorrendo todos os objetos pela referência "funcionario",
cada objeto sabe qual classe o criou.

Assim:
- Funcionario usa bônus de 10%
- Gerente usa bônus de 20%
- Estagiario usa bônus de 5%

O Python faz isso dinamicamente em tempo de execução,
sem necessidade de usar if, type() ou isinstance()."""