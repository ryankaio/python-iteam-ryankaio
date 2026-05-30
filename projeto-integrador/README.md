# Urna Eletrônica — Sistema de Votação em Python

Simulação de uma urna eletrônica desenvolvida em Python com foco em **Programação Orientada a Objetos**, encapsulamento, herança e tratamento robusto de exceções.

---

## Sumário

- [Visão Geral](#visão-geral)
- [Estrutura de Classes](#estrutura-de-classes)
- [Requisitos de Negócio Atendidos](#requisitos-de-negócio-atendidos)
- [Requisitos Técnicos Atendidos](#requisitos-técnicos-atendidos)
- [Como Executar](#como-executar)
- [Fluxo de Uso](#fluxo-de-uso)
- [Dados Pré-carregados](#dados-pré-carregados)
- [Exemplos de Sessão](#exemplos-de-sessão)

---

## Visão Geral

O sistema simula uma eleição eletrônica com múltiplos candidatos e eleitores cadastrados previamente. O operador inicia a urna e os eleitores votam individualmente. Ao digitar `0` como número do candidato, o operador encerra a votação e o relatório de apuração é exibido automaticamente.

---

## Estrutura de Classes

```
Pessoa  (classe base)
├── Candidato   — número, partido, contador de votos (encapsulado)
└── Eleitor     — identificação, status de votação (encapsulado)

Voto            — artefato de sigilo; armazena apenas número do candidato + horário
Relatorio       — geração e exibição da apuração final
Urna            — classe principal; gerencia todo o fluxo de votação
```

### Diagrama de herança

```
         ┌──────────┐
         │  Pessoa  │  _nome
         └────┬─────┘
       ┌──────┴──────┐
       ▼             ▼
  Candidato       Eleitor
  __numero        __identificacao
  __partido       __votou
  __total_votos
```

### Responsabilidades por classe

| Classe | Responsabilidade |
|---|---|
| `Pessoa` | Atributo `_nome` compartilhado; base para herança |
| `Candidato` | Armazena dados do candidato e contagem interna de votos |
| `Eleitor` | Controla identidade e status de votação de cada eleitor |
| `Voto` | Registra voto de forma sigilosa (sem vínculo com eleitor) |
| `Relatorio` | Gera apuração com ranking, percentuais e vencedor |
| `Urna` | Orquestra candidatos, eleitores, votos e relatório |

---

## Requisitos de Negócio Atendidos

### 2.1 Gestão de Candidatos
- 5 candidatos pré-carregados com número, nome e partido.
- Listagem exibida antes de cada voto.

### 2.2 Gestão de Eleitores
- 7 eleitores pré-carregados com CPF simplificado e nome.
- Controle de voto duplicado via atributo `__votou` encapsulado.
- **Sigilo do voto**: a classe `Voto` armazena apenas o número do candidato, nunca o nome ou identificação do eleitor.

### 2.3 Fluxo de Votação
1. Sistema solicita CPF do eleitor.
2. Verifica existência no cadastro.
3. Verifica se já votou.
4. Exibe candidatos disponíveis.
5. Eleitor digita o número do candidato.
6. Sistema valida o número.
7. Voto é registrado de forma sigilosa; status do eleitor atualizado.
8. Confirmação exibida; sistema aguarda próximo eleitor.
- Encerramento disponível a qualquer momento digitando `0`.

### 2.4 Apuração e Resultados
- Total de eleitores habilitados.
- Total de votos registrados.
- Percentual de participação e abstenções.
- Votos por candidato em ordem decrescente.
- Percentual de cada candidato.
- Nome do vencedor — ou indicação de empate com nota sobre critério de desempate.

---

## Requisitos Técnicos Atendidos

### 3.1 Programação Orientada a Objetos
Toda a lógica está encapsulada em classes. Não há variáveis globais nem funções soltas.

### 3.2 Encapsulamento
| Atributo | Classe | Proteção |
|---|---|---|
| `__total_votos` | `Candidato` | name mangling (`__`) |
| `__votou` | `Eleitor` | name mangling (`__`) |
| `__candidatos` | `Urna` | name mangling (`__`) |
| `__eleitores` | `Urna` | name mangling (`__`) |
| `__urna_votos` | `Urna` | name mangling (`__`) |

Acesso externo somente via `@property` somente-leitura. Modificação apenas via métodos internos protegidos (`_registrar_voto`, `_marcar_como_votante`).

### 3.3 Herança
`Candidato` e `Eleitor` herdam de `Pessoa`, reaproveitando o atributo `_nome` e o método `__str__` base.

### 3.4 Tratamento de Exceções
| Cenário | Exceção customizada |
|---|---|
| Eleitor não cadastrado | `EleitorNaoCadastradoError` |
| Eleitor já votou | `EleitorJaVotouError` |
| Número de candidato inválido | `CandidatoInvalidoError` |
| Entrada não numérica | `ValueError` capturado com `try/except` |

Todos os erros exibem mensagem clara e o fluxo continua sem traceback.

---

## Como Executar

### Pré-requisitos
- Python 3.10 ou superior (uso de `list[Tipo]` como type hint nativo).

### Execução
```bash
python urna_eletronica.py
```

Não há dependências externas. Nenhuma instalação adicional é necessária.

---

## Fluxo de Uso

```
Iniciar programa
    │
    ▼
Sistema exibe boas-vindas e total de eleitores
    │
    ▼
Solicita CPF do eleitor ◄────────────────────────────────┐
    │                                                     │
    ├── CPF inválido → mensagem de erro ──────────────────┤
    ├── Eleitor já votou → mensagem de erro ──────────────┤
    │                                                     │
    ▼                                                     │
Exibe lista de candidatos                                 │
    │                                                     │
    ▼                                                     │
Solicita número do candidato                             │
    │                                                     │
    ├── "0" → encerrar votação → exibe relatório → fim    │
    ├── Entrada não numérica → mensagem de erro ──────────┤
    ├── Candidato inexistente → mensagem de erro ─────────┤
    │                                                     │
    ▼                                                     │
Voto registrado (sigiloso) + eleitor marcado ────────────┘
```

---

## Dados Pré-carregados

### Candidatos

| Número | Nome | Partido |
|---|---|---|
| 10 | Ana Beatriz Silva | Partido da Esperança - PE |
| 20 | Carlos Eduardo Mendes | Frente Popular Unida - FPU |
| 30 | Fernanda Gomes Costa | Movimento Renovação - MR |
| 40 | Ricardo Lemos Pinto | Aliança Democrática - AD |
| 50 | Patrícia Souza Lima | Coligação Progresso - CP |

### Eleitores

| CPF | Nome |
|---|---|
| 001.234.567-00 | João Pedro Alves |
| 002.345.678-11 | Maria Clara Ferreira |
| 003.456.789-22 | Lucas Henrique Santos |
| 004.567.890-33 | Juliana Rocha Pimentel |
| 005.678.901-44 | Roberto Augusto Neves |
| 006.789.012-55 | Camila Andrade Torres |
| 007.890.123-66 | Diego Martins Barbosa |

---

## Exemplos de Sessão

### Voto bem-sucedido
```
  Informe sua identificação (CPF): 001.234.567-00

  Bem-vindo(a)! Você está habilitado(a) a votar.

  ┌─ CANDIDATOS DISPONÍVEIS ───────────────────────┐
  │  [10] Ana Beatriz Silva (Partido da Esperança - PE)
  │  [20] Carlos Eduardo Mendes (Frente Popular Unida - FPU)
  │  [30] Fernanda Gomes Costa (Movimento Renovação - MR)
  │  [40] Ricardo Lemos Pinto (Aliança Democrática - AD)
  │  [50] Patrícia Souza Lima (Coligação Progresso - CP)
  │  [ 0] Encerrar votação (operador)
  └────────────────────────────────────────────────┘

  Digite o número do candidato: 10

  ✔  Voto registrado com sucesso! Obrigado(a) por participar.
     Total de votos até agora: 1
```

### Tentativa de voto duplo
```
  Informe sua identificação (CPF): 001.234.567-00
  ✗  O eleitor já exerceu seu voto nesta eleição.
```

### Entrada inválida
```
  Digite o número do candidato: abc
  ✗  Entrada inválida: 'abc' não é um número. Tente novamente.
```

### Relatório final (exemplo)
```
════════════════════════════════════════════════════
          RELATÓRIO DE APURAÇÃO FINAL
════════════════════════════════════════════════════
  Eleitores habilitados : 7
  Votos registrados     : 5
  Participação          : 71.4%
  Abstenções            : 2

  Candidato                      Votos       %
  ──────────────────────────────────────────────
  [10] Ana Beatriz Silva         2       40.0%
  [20] Carlos Eduardo Mendes     2       40.0%
  [30] Fernanda Gomes Costa      1       20.0%
  [40] Ricardo Lemos Pinto       0        0.0%
  [50] Patrícia Souza Lima       0        0.0%
════════════════════════════════════════════════════

  ⚠️  EMPATE entre: Ana Beatriz Silva (PE), Carlos Eduardo Mendes (FPU)
      O critério de desempate será definido pelo regulamento.

════════════════════════════════════════════════════
```

