# Teste de Performance: Strings vs Booleanos em SQL

Este projeto realiza um experimento simples para comparar o tempo de execução entre consultas SQL filtrando por valores do tipo texto (`"Sim"` / `"Não"`) e valores booleanos (`True` / `False`) usando **Python + SQLite**.

---

## Objetivo

Demonstrar que, em bancos de dados, utilizar valores booleanos pode ser **mais eficiente** do que strings para representar estados binários.

---

## Como rodar o projeto

1. Clone o repositório:

bash
git clone https://github.com/Kauadevv/teste-booleanos-sqlite.git
cd teste-booleanos-sqlite


2. Instale o matplotlib:

pip install matplotlib

3. Execute o script

python teste_booleanos.py
O script insere 1 milhão de registros e mede o tempo de execução das queries.

## Resultado
A consulta com valores booleanos foi ligeiramente mais rápida.

Boas práticas aplicadas ^_^
Uso de SQLite para facilitar testes locais

Códigos organizados e comentados

Arquivos desnecessários ignorados via .gitignore

Observação
Em bancos maiores (milhões a bilhões de registros), o uso de tipos corretos (como booleanos) pode melhorar performance
e economia de espaço. Esse experimento serve como base para essa discussão.

