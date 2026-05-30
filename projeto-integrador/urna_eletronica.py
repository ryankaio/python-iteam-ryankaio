# Projeto Integrador — Urna Eletrônica
# Aluno: (Ryan Kaio Sena da Silva)

# ── Escreva sua solução abaixo ──────────────────────────────────────

"""
Urna Eletrônica - Sistema de Votação
Projeto orientado a objetos com encapsulamento, herança e tratamento de exceções.
"""

from datetime import datetime


# ─────────────────────────────────────────────
# Exceções customizadas
# ─────────────────────────────────────────────

class EleitorNaoCadastradoError(Exception):
    """Eleitor não encontrado no cadastro."""


class EleitorJaVotouError(Exception):
    """Eleitor já exerceu seu direito de voto."""


class CandidatoInvalidoError(Exception):
    """Número de candidato não encontrado."""


class VotacaoEncerradaError(Exception):
    """Votação já foi encerrada."""


# ─────────────────────────────────────────────
# Classe base: Pessoa
# ─────────────────────────────────────────────

class Pessoa:
    """Classe base que representa uma pessoa com nome."""

    def __init__(self, nome: str):
        self._nome = nome.strip()

    @property
    def nome(self) -> str:
        return self._nome

    def __str__(self) -> str:
        return self._nome


# ─────────────────────────────────────────────
# Candidato (herda de Pessoa)
# ─────────────────────────────────────────────

class Candidato(Pessoa):
    """Representa um candidato na eleição."""

    def __init__(self, numero: int, nome: str, partido: str):
        super().__init__(nome)
        self.__numero = numero
        self.__partido = partido.strip()
        self.__total_votos = 0          # encapsulado — só a Urna altera

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def partido(self) -> str:
        return self.__partido

    @property
    def total_votos(self) -> int:
        return self.__total_votos

    def _registrar_voto(self) -> None:
        """Método protegido: chamado apenas pela Urna."""
        self.__total_votos += 1

    def __str__(self) -> str:
        return f"[{self.__numero:02d}] {self._nome} ({self.__partido})"


# ─────────────────────────────────────────────
# Eleitor (herda de Pessoa)
# ─────────────────────────────────────────────

class Eleitor(Pessoa):
    """Representa um eleitor habilitado."""

    def __init__(self, identificacao: str, nome: str):
        super().__init__(nome)
        self.__identificacao = str(identificacao).strip()
        self.__votou = False            # encapsulado — só a Urna altera

    @property
    def identificacao(self) -> str:
        return self.__identificacao

    @property
    def votou(self) -> bool:
        return self.__votou

    def _marcar_como_votante(self) -> None:
        """Método protegido: chamado apenas pela Urna após registro do voto."""
        self.__votou = True

    def __str__(self) -> str:
        status = "✓ votou" if self.__votou else "pendente"
        return f"Eleitor {self.__identificacao} — {self._nome} [{status}]"


# ─────────────────────────────────────────────
# Voto (artefato de sigilo)
# ─────────────────────────────────────────────

class Voto:
    """Registra um voto de forma sigilosa: armazena apenas o número do candidato e o horário."""

    def __init__(self, numero_candidato: int):
        self.__numero_candidato = numero_candidato
        self.__horario = datetime.now()

    @property
    def numero_candidato(self) -> int:
        return self.__numero_candidato

    @property
    def horario(self) -> datetime:
        return self.__horario


# ─────────────────────────────────────────────
# Relatório
# ─────────────────────────────────────────────

class Relatorio:
    """Gera e exibe o relatório de apuração."""

    @staticmethod
    def gerar(candidatos: list[Candidato], total_eleitores: int) -> None:
        total_votos = sum(c.total_votos for c in candidatos)
        participacao = (total_votos / total_eleitores * 100) if total_eleitores > 0 else 0
        ranking = sorted(candidatos, key=lambda c: c.total_votos, reverse=True)

        separador = "═" * 52
        print(f"\n{separador}")
        print("          RELATÓRIO DE APURAÇÃO FINAL")
        print(separador)
        print(f"  Eleitores habilitados : {total_eleitores}")
        print(f"  Votos registrados     : {total_votos}")
        print(f"  Participação          : {participacao:.1f}%")
        print(f"  Abstenções            : {total_eleitores - total_votos}")
        print(f"\n  {'Candidato':<30} {'Votos':>6} {'%':>7}")
        print("  " + "─" * 46)

        for c in ranking:
            pct = (c.total_votos / total_votos * 100) if total_votos > 0 else 0
            print(f"  {str(c):<30} {c.total_votos:>6} {pct:>6.1f}%")

        print(separador)

        if total_votos == 0:
            print("  Nenhum voto foi registrado.")
        else:
            max_votos = ranking[0].total_votos
            vencedores = [c for c in ranking if c.total_votos == max_votos]

            if len(vencedores) == 1:
                print(f"\n  🏆  VENCEDOR: {vencedores[0].nome} ({vencedores[0].partido})")
            else:
                nomes = ", ".join(f"{c.nome} ({c.partido})" for c in vencedores)
                print(f"\n  ⚠️  EMPATE entre: {nomes}")
                print("      O critério de desempate será definido pelo regulamento.")

        print(f"{separador}\n")


# ─────────────────────────────────────────────
# Urna (classe principal)
# ─────────────────────────────────────────────

class Urna:
    """
    Sistema principal de votação eletrônica.
    Gerencia candidatos, eleitores e o fluxo de votação.
    """

    SENHA_ENCERRAMENTO = "0"

    def __init__(self):
        self.__candidatos: dict[int, Candidato] = {}   # encapsulado
        self.__eleitores: dict[str, Eleitor] = {}      # encapsulado
        self.__urna_votos: list[Voto] = []             # encapsulado — sigilo
        self.__encerrada = False
        self.__relatorio = Relatorio()

        self._carregar_candidatos()
        self._carregar_eleitores()

    # ── Carga inicial ──────────────────────────────────────────

    def _carregar_candidatos(self) -> None:
        dados = [
            (10, "Ana Beatriz Silva",     "Partido da Esperança - PE"),
            (20, "Carlos Eduardo Mendes", "Frente Popular Unida - FPU"),
            (30, "Fernanda Gomes Costa",  "Movimento Renovação - MR"),
            (40, "Ricardo Lemos Pinto",   "Aliança Democrática - AD"),
            (50, "Patrícia Souza Lima",   "Coligação Progresso - CP"),
        ]
        for numero, nome, partido in dados:
            candidato = Candidato(numero, nome, partido)
            self.__candidatos[numero] = candidato

    def _carregar_eleitores(self) -> None:
        dados = [
            ("001.234.567-00", "João Pedro Alves"),
            ("002.345.678-11", "Maria Clara Ferreira"),
            ("003.456.789-22", "Lucas Henrique Santos"),
            ("004.567.890-33", "Juliana Rocha Pimentel"),
            ("005.678.901-44", "Roberto Augusto Neves"),
            ("006.789.012-55", "Camila Andrade Torres"),
            ("007.890.123-66", "Diego Martins Barbosa"),
        ]
        for cpf, nome in dados:
            eleitor = Eleitor(cpf, nome)
            self.__eleitores[cpf] = eleitor

    # ── Propriedades de consulta (somente leitura) ──────────────

    @property
    def total_eleitores(self) -> int:
        return len(self.__eleitores)

    @property
    def total_votos(self) -> int:
        return len(self.__urna_votos)

    # ── Exibição ────────────────────────────────────────────────

    def _exibir_candidatos(self) -> None:
        print("\n  ┌─ CANDIDATOS DISPONÍVEIS ───────────────────────┐")
        for c in self.__candidatos.values():
            print(f"  │  {c}")
        print(f"  │  [{self.SENHA_ENCERRAMENTO:>2}] Encerrar votação (somente operador)")
        print("  └────────────────────────────────────────────────┘")

    # ── Validações ──────────────────────────────────────────────

    def _verificar_eleitor(self, identificacao: str) -> Eleitor:
        eleitor = self.__eleitores.get(identificacao)
        if eleitor is None:
            raise EleitorNaoCadastradoError(
                f"Identificação '{identificacao}' não encontrada no cadastro."
            )
        if eleitor.votou:
            raise EleitorJaVotouError(
                f"O eleitor já exerceu seu voto nesta eleição."
            )
        return eleitor

    def _verificar_candidato(self, numero: int) -> Candidato:
        candidato = self.__candidatos.get(numero)
        if candidato is None:
            raise CandidatoInvalidoError(
                f"Número {numero} não corresponde a nenhum candidato."
            )
        return candidato

    # ── Registro de voto (sigiloso) ─────────────────────────────

    def _registrar_voto(self, eleitor: Eleitor, candidato: Candidato) -> None:
        voto = Voto(candidato.numero)
        self.__urna_votos.append(voto)
        candidato._registrar_voto()       # incrementa contador interno
        eleitor._marcar_como_votante()    # atualiza status

    # ── Fluxo de votação ────────────────────────────────────────

    def iniciar_votacao(self) -> None:
        print("\n" + "═" * 52)
        print("       URNA ELETRÔNICA — BEM-VINDO(A)!")
        print("═" * 52)
        print(f"  Eleitores habilitados: {self.total_eleitores}")
        print("  Digite 'sair' no CPF ou '0' no candidato para encerrar.")

        while not self.__encerrada:
            try:
                self._ciclo_votacao()
            except EOFError:
                # Encerramento forçado (ex.: pipe de teste fechado)
                self._encerrar()

    def _ciclo_votacao(self) -> None:
        print("\n" + "─" * 52)
        identificacao = input("  Informe sua identificação (CPF) [ou 'sair']: ").strip()

        if identificacao.lower() == "sair":
            self._encerrar()
            return

        if not identificacao:
            print("  ⚠  Identificação não pode estar em branco.")
            return

        # Validar eleitor
        try:
            eleitor = self._verificar_eleitor(identificacao)
        except EleitorNaoCadastradoError as e:
            print(f"  ✗  {e}")
            return
        except EleitorJaVotouError as e:
            print(f"  ✗  {e}")
            return

        print(f"\n  Bem-vindo(a)! Você está habilitado(a) a votar.")
        self._exibir_candidatos()

        # Receber número do candidato
        entrada = input("\n  Digite o número do candidato: ").strip()

        # Verificar encerramento pelo operador
        if entrada == self.SENHA_ENCERRAMENTO:
            self._encerrar()
            return

        # Validar entrada numérica
        try:
            numero = int(entrada)
        except ValueError:
            print(f"  ✗  Entrada inválida: '{entrada}' não é um número. Tente novamente.")
            return

        # Validar candidato
        try:
            candidato = self._verificar_candidato(numero)
        except CandidatoInvalidoError as e:
            print(f"  ✗  {e}")
            return

        # Registrar voto
        self._registrar_voto(eleitor, candidato)
        print(f"\n  ✔  Voto registrado com sucesso! Obrigado(a) por participar.")
        print(f"     Total de votos até agora: {self.total_votos}")

    # ── Encerramento ────────────────────────────────────────────

    def _encerrar(self) -> None:
        self.__encerrada = True
        print("\n  Votação encerrada pelo operador.")
        self.__relatorio.gerar(
            list(self.__candidatos.values()),
            self.total_eleitores
        )


# ─────────────────────────────────────────────
# Ponto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    urna = Urna()
    urna.iniciar_votacao()
