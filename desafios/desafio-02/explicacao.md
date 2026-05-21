# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _(Ryan Kaio Sena da Silva)_
**Data:** _(2026-05-20)_

---

## O que meu programa faz

_(O programa pede para o usuario irformar alguns dados, seu nome, peso e altura, assim que que o programa coleta as informações, uma função para calcular o IMC (Índice de Massa Corporal), ao final do programa é entregado uma mensagem com o nome e o IMC do usuario.)_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_(Os `input()` por padrão sempre retorna o valor em `str()`, como iremos realizar calculos matematicos, precisaremos converter esses valores para numeros, porém, a conversão não poder ser para `int()`, porque `int()` aceita apenas numeros inteiros, assim podendo da erro no programa, para isso usaremos o `float()`,assim podemos usar numeros decimais sem problemas, pois altura e peso quase sempre possuem numeros decimais.)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
