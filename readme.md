# 🏦 Sistema Bancário Simples (Python)

Este é um projeto de **sistema bancário em Python** desenvolvido para simular operações básicas de conta corrente, como **depósito, saque, extrato, criação de usuários e contas**.  
O objetivo é exercitar conceitos de **lógica de programação**, **estruturas de repetição**, **condicionais**, **funções** e **manipulação de listas e dicionários**.

---

## 🚀 Funcionalidades

O sistema apresenta um menu interativo com as seguintes opções:

- **[d] Depósito** → Permite adicionar saldo à conta.
- **[s] Saque** → Realiza um saque, com regras:
  - Limite de **R$ 500,00 por operação**
  - Máximo de **3 saques diários**
  - Não permite saque maior que o saldo disponível
- **[e] Extrato** → Mostra todas as movimentações realizadas e o saldo atual.
- **[nu] Novo Usuário** → Cadastra um cliente com CPF, nome, data de nascimento e endereço.
- **[nc] Nova Conta** → Cria uma conta vinculada a um usuário já cadastrado.
- **[lc] Listar Contas** → Exibe todas as contas cadastradas no sistema.
- **[q] Sair** → Finaliza a execução do sistema.

---

## 📋 Regras do Sistema

- Saldo inicial: **R$ 0,00**
- O depósito só é permitido com valores **maiores que zero**
- O saque só é permitido se:
  - O valor não ultrapassar o saldo
  - O valor não ultrapassar **R$ 500,00**
  - O número de saques for **menor que 3 por dia**
- O extrato lista todas as operações realizadas (**depósitos e saques**)
- Para criar uma conta é necessário **ter um usuário previamente cadastrado**
- Cada conta criada recebe:
  - Agência padrão: **0001**
  - Número de conta sequencial (1, 2, 3, ...)

---

## 📂 Estrutura do Código

- `menu()` → Apresenta as opções disponíveis para o usuário
- `depositar()` → Realiza depósitos e atualiza saldo e extrato
- `sacar()` → Gerencia os saques, respeitando regras de limite e quantidade
- `exibir_extrato()` → Mostra todas as movimentações e saldo atual
- `criar_usuario()` → Cadastra um novo cliente no sistema
- `filtrar_usuario()` → Verifica se o CPF informado já existe
- `criar_conta()` → Cria uma conta vinculada a um usuário existente
- `listar_contas()` → Exibe todas as contas cadastradas
- `main()` → Função principal que executa o loop do programa
