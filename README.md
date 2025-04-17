# Algoritmo de Karatsuba - Multiplicação Rápida de Inteiros

## Descrição

Este projeto implementa o **algoritmo de Karatsuba**, que é uma técnica eficiente para multiplicação de inteiros grandes. O algoritmo de Karatsuba melhora a eficiência da multiplicação convencional (que tem complexidade \(O(n^2)\)) reduzindo-a para aproximadamente \(O(n^{\log_2{3}}) \approx O(n^{1.585})\), o que torna a multiplicação de grandes números muito mais rápida.

A implementação é feita em Python e é capaz de multiplicar dois números inteiros grandes de forma recursiva, dividindo-os em partes menores e usando três multiplicações recursivas para obter o resultado final.

## Objetivo

O objetivo deste projeto é demonstrar a aplicação do algoritmo de Karatsuba em um caso de multiplicação de dois inteiros grandes. Este código pode ser utilizado para estudar e compreender como o algoritmo de Karatsuba funciona na prática e como ele é mais eficiente que a multiplicação tradicional.

## Funcionalidade

- **Multiplicação de dois inteiros grandes** utilizando o algoritmo de Karatsuba.
- **Entrada de dados interativa**: o usuário fornece dois números inteiros e o programa calcula e exibe o resultado da multiplicação.
- **Tratamento de exceções**: verifica se os números fornecidos são válidos (inteiros não-negativos).

## Como Usar

### Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária.

### Executando o Código

1. Clone ou baixe o repositório.
2. Abra o terminal e navegue até a pasta onde o arquivo `karatsuba.py` está localizado.
3. Execute o script:

```bash
python karatsuba.py