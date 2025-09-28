# 🏦 Sistema Bancário Orientado a Objetos (Python)

Este é um projeto de **sistema bancário em Python** desenvolvido com **Programação Orientada a Objetos (POO)** para simular operações de conta corrente, como **depósito, saque, extrato, criação de usuários e contas**.  
O objetivo é exercitar conceitos de **classes, herança, métodos, propriedades, listas, funções e abstração com `ABC`**.

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

### 📌 Classes principais

- `Usuario` → Representa o cliente genérico (endereço, contas).
- `Pessoa` → Representa pessoa física (nome, nascimento, CPF).
- `ContaBancaria` → Classe base com saldo, depósitos, saques e histórico.
- `ContaComum` → Conta corrente com limites de saque e número máximo de operações.
- `Historico` → Armazena todas as transações realizadas.
- `Movimento` → Classe abstrata para representar uma transação.
- `Deposito` → Transação de depósito.
- `Saque` → Transação de saque.

### 📌 Funções auxiliares

- `mostrar_menu()` → Apresenta as opções disponíveis para o usuário.
- `realizar_deposito()` → Realiza depósitos em uma conta.
- `realizar_saque()` → Efetua saques respeitando regras de limite e quantidade.
- `exibir_extrato()` → Exibe todas as movimentações e o saldo atual.
- `criar_usuario()` → Cadastra um novo cliente no sistema.
- `localizar_usuario()` → Busca um usuário pelo CPF.
- `criar_conta()` → Cria uma conta vinculada a um usuário existente.
- `listar_contas()` → Mostra todas as contas cadastradas.
- `main()` → Função principal que executa o loop do programa.
