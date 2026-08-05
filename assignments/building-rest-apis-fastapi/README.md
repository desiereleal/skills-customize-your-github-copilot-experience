# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST funcional usando FastAPI, aplicando conceitos de rotas, validacao com Pydantic e codigos de status HTTP. Ao final, voce tera uma base clara para criar servicos backend em Python.

## 📝 Tarefas

### 🛠️ Criar Endpoints CRUD para Itens

#### Descrição
Implemente uma API para gerenciar itens (produtos, tarefas ou livros), com operacoes de criar, listar, buscar por ID, atualizar e remover.

#### Requisitos
O programa concluido deve:

- Criar um endpoint `GET /health` que retorne status da API.
- Implementar `POST /items` para criar um item com `name`, `description` e `price`.
- Implementar `GET /items` para listar todos os itens cadastrados.
- Implementar `GET /items/{item_id}` para buscar um item pelo ID e retornar `404` quando nao existir.
- Implementar `PUT /items/{item_id}` para atualizar os dados de um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item e retornar `204` em caso de sucesso.

### 🛠️ Validar Dados e Tratar Erros

#### Descrição
Use modelos Pydantic para validar os dados de entrada e padronize respostas de erro para melhorar a confiabilidade da API.

#### Requisitos
O programa concluido deve:

- Definir modelos Pydantic para entrada (`ItemCreate`) e saida (`Item`).
- Validar que `name` nao seja vazio e que `price` seja maior que zero.
- Retornar `422` automaticamente para payload invalido.
- Retornar mensagens claras em erros de negocio (por exemplo, item nao encontrado).
- Organizar o codigo de forma legivel para facilitar manutencao e testes futuros.
