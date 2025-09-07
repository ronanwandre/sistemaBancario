# 🏦 Sistema Bancário Simples (Python)

Este é um projeto de **sistema bancário em Python** desenvolvido para simular operações básicas de conta corrente, como **depósito, saque, extrato** e **sair**.  
O objetivo é exercitar conceitos de **lógica de programação**, **estruturas de repetição**, **condicionais** e **manipulação de variáveis**.

---

## 🚀 Funcionalidades

O sistema apresenta um menu interativo com as seguintes opções:

- **[d] Depósito** → Permite adicionar saldo à conta.
- **[s] Saque** → Realiza um saque, com regras:
  - Limite de **R$ 500,00 por operação**
  - Máximo de **3 saques diários**
  - Não permite saque maior que o saldo disponível
- **[e] Extrato** → Mostra todas as movimentações realizadas e o saldo atual.
- **[0] Sair** → Finaliza a execução do sistema.

---

## 📋 Regras do Sistema

- Saldo inicial: **R$ 0,00**
- O depósito só é permitido com valores **maiores que zero**
- O saque só é permitido se:
  - O valor não ultrapassar o saldo
  - O valor não ultrapassar **R$ 500,00**
  - O número de saques for **menor que 3 por dia**
- O extrato lista todas as operações realizadas (**depósitos e saques**)

---

## 📂 Estrutura do Código

- `menu` → String que apresenta as opções ao usuário
- `saldo` → Armazena o valor disponível em conta
- `limite` → Define o valor máximo permitido por saque
- `extrato` → Registra o histórico de movimentações
- `numero_saques` → Conta o número de saques realizados
- `LIMITE_SAQUES` → Define o máximo de saques possíveis
