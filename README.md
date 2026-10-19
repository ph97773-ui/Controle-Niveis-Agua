# Controle de Níveis de Água

Este projeto simula o monitoramento de um reservatório de água no terminal.

O programa possui cinco níveis. Cada nível apresenta uma mensagem diferente e uma cor usando a biblioteca `colorama`:

- Nível 1: muito baixo (crítico) — vermelho
- Nível 2: baixo — amarelo
- Nível 3: médio — verde
- Nível 4: alto — ciano
- Nível 5: muito alto (alerta) — azul

## Como executar

Instale a biblioteca:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python app.py
```

A simulação mostra os cinco níveis em sequência. A função `cor_do_nivel()` escolhe a cor da mensagem e `Style.RESET_ALL` restaura o estilo do terminal depois de cada exibição.

## Tecnologias

- Python
- Colorama
- Listas
- Funções

## Autor

Paulo Henrique L. Rodrigues
