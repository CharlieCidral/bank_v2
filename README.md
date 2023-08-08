# bank_v2
Learning functions in python with Dio, but with some increments.

### SIGN PAGE

![image](https://github.com/CharlieCidral/bank_v2/assets/69029099/ab8adb53-f5c4-41b4-8311-a24d1ea9c1f8)

### MENU

![image](https://github.com/CharlieCidral/bank_v2/assets/69029099/4805d1a1-a9fb-45b0-8204-2d21c75ab41f)

### Proposed challenge

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

### Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizañhiStórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

### Separação em Funções

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O
retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.( Exercitar os argumentos por posição e argumentos nomeados )

### Saque

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero saques, limite_saques. Sugestão de retorno: saldo e extrato.

### Depósito

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

### Extrato

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

### Novas funções

Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

### Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro-bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.( Estrutura de dados para armazenar chave/valor )

### Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

### Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

