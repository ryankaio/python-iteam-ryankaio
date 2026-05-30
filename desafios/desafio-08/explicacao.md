# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(Ryan Kaio Sena da Silva)_
**Data:** _(29/05/2026)_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

_(O saldo deve ser um atributo da instância (self.saldo) porque ele representa o estado da conta bancária. Esse valor precisa ser armazenado e permanecer disponível durante toda a vida do objeto, quando usamos (self.saldo = saldo_inicial) o saldo fica associado àquela conta específica. Assim, qualquer alteração feita por depositar() ou sacar() é mantida para as próximas operações. Se o saldo fosse uma variável comum dentro de um método, ela existiria apenas durante a execução daquele método, A variável saldo é criada quando o método começa é destruída quando o método termina, nenhum outro método consegue acessar esse valor.)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
