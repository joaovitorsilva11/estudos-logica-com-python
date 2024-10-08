# -*- coding: utf-8 -*-
"""Cópia de PythonBasico_ListaRevisao_ProgWeb_Resolvidas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m3ZZKeDB-T5FdtIQiBS2Gn_SEqVtnbga

# Primeiro trimestre - Revisão Python


Exercícios para treinar sintaxe e uso básico da linguagem Python.
Os exercícios desta lista são auto-corrigíveis.

## Lista 1 - Variáveis e inicialização de listas e dicionários

### exercicio 1

Na linha abaixo, crie uma variável chamada **on_mars_right_now** e atribua a ela o valor booleano **False**
"""

on_mars_right_now = False

assert on_mars_right_now == False, "Se você ver um 'Name Error', certifique-se de criar a variável e atribuir um valor."
print("Exercício 1 está correto.")

"""### Exercício 2

Crie uma variável chamada **fruits** e atribua a ela uma lista de frutas contendo os seguintes nomes de frutas como strings:
**manga, banana, goiaba, kiwi e morango.**
"""

fruits = ["manga", "banana", "goiaba", "kiwi", "morango"]

assert fruits == ["manga", "banana", "goiaba", "kiwi", "morango"], "Se você ver um erro de assert, verifique se a variável contém todas as strings na ordem fornecida"
print("Exercício 2 está correto.")

"""### exercicio 3

Crie uma variável chamada **vegetables** e atribua a ela uma lista de vegetais contendo os seguintes nomes de vegetais como strings:
**berinjela, brócolis, cenoura, couve-flor e abobrinha**
"""

vegetables = ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha"]

assert vegetables == ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha"], "Certifique-se de que a variável contenha todas as strings na ordem fornecida"
print("Exercício 3 está correto.")

"""### exercicio 4

Crie uma variável chamada **numbers** e atribua a ela uma lista de números: **1, 2, 3, 4, 5, 6, 7, 8, 9, 10**
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Certifique-se de que a variável contenha os números de 1 a 10 na ordem."
print("Exercício 4 está correto.")

"""### exercicio 5

Dada a seguinte atribuição da lista de frutas, adicione **"tomate"** ao final da lista.
"""

fruits.append("tomate")

assert fruits == ["manga", "banana", "goiaba", "kiwi", "morango", "tomate"], "Certifique-se de que a variável contenha todas as strings na ordem correta"
print("Exercício 5 está correto")

"""### exercicio 6

Dada a seguinte atribuição da lista de vegetais, adicione **"tomate"** ao final da lista.
"""
vegetables.append("tomate")


assert vegetables == ["berinjela", "brócolis", "cenoura", "couve-flor", "abobrinha", "tomate"], "Certifique-se de que a variável contenha todas as strings na ordem fornecida"
print("Exercício 6 está correto")

"""### exercicio 7

Dada a lista de números definida abaixo, **inverta a lista** de números que você criou acima.
"""

numbers.reverse()

assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "O erro de assert significa que a resposta está incorreta."
print("Exercício 7 está correto.")

"""### exercicio 8

**Ordene** os vegetais em ordem alfabética
"""

vegetables = sorted(vegetables)

assert vegetables == ['abobrinha', 'berinjela', 'brócolis', 'cenoura', 'couve-flor', 'tomate']
print("Exercício 8 está correto.")

"""### exercicio 9

Escreva o código necessário para **classificar** as frutas em ordem alfabética inversa
"""

fruits.sort(reverse=True)

assert fruits == ['tomate', 'morango', 'manga', 'kiwi', 'goiaba', 'banana']
print("Exercício 9 está correto.")

"""### exercicio 10

Escreva o código necessário para produzir uma única lista que contenha todas as frutas e depois todos os vegetais na ordem em que foram classificados acima.
"""

fruits_and_veggies = fruits + vegetables

assert fruits_and_veggies == ['tomate', 'morango', 'manga', 'kiwi', 'goiaba', 'banana', 'abobrinha', 'berinjela', 'brócolis', 'cenoura', 'couve-flor', 'tomate']
print("Exercício 10 está correto")
