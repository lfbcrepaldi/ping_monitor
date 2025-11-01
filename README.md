# Ping Monitor

Ferramenta simples para monitorar o tempo de resposta (latência) de múltiplos hosts — equivalente a executar vários `ping -t` do Windows em paralelo.

## O que é

Este projeto foi desenvolvido com o objetivo de checar o tempo de resposta de múltiplas redes/hosts ao mesmo tempo. Ele realiza pings periódicos (com timeout configurável) e exibe uma tabela ao vivo com a latência de cada host.

## Principais características

- Exibe uma tabela atualizada ao vivo com latências em milissegundos.
- Marca estados por cor (verde, amarelo, vermelho) conforme a latência ou timeout.
- Fácil de configurar e executar.

## Requisitos

- Dependências listadas em `requirements.txt` (ex.: `ping3`, `rich`).

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o script principal:

```bash
python main.py
```

Em Linux, se retornar erro **PermissionError** use `sudo <python-command> main.py` (exemplo: `sudo python3 main.py`)

Use Ctrl+C para encerrar.

## Observações

- O script utiliza a biblioteca `ping3` para realizar os pings e `rich` para renderizar a tabela ao vivo.
- Altere a lista de hosts diretamente no arquivo `main.py` conforme necessário.