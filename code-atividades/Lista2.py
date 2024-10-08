"""## Lista 2 - Funções e operações numéricas

### Utilitarios

alguns utilitarios disponibilizados pelo professor e adaptado por mim para seguir minha necessidade e logica
"""

import random

par_positivo = random.randrange(2,101,2)
print("O número randomico par e positivo é: ", par_positivo)

import random

par_negativo = random.randrange(-100,-1,2)
print("O número randomico par e negativo é: ", par_negativo)

import random

impar_positivo = random.randrange(1, 100, 2)
print("O número randomico ímpar e positivo é: ", impar_positivo)

import random

impar_negativo = random.randrange(-101,0,2)
print("O número randomico ímpar e negativo é: ", impar_negativo)

"""### exercicio 1

Escreva uma **definição de função** para uma função chamada **add_one** que **recebe um número** e retorna esse **número mais um**.
"""
def add_one(number):
   number += 1
   return number

assert add_one(2) == 3, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert add_one(0) == 1, "Zero mais um é um."
assert add_one(par_positivo) == par_positivo + 1, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert add_one(impar_negativo) == impar_negativo + 1, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 1 está correto.")

"""### exercicio 2

Escreva uma **definição de função** chamada ***is_positive*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for positivo**.
"""

def is_positive(number):
   if number > 0:
      return True
   else:
      return False

assert is_positive(impar_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(par_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(impar_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(par_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_positive(0) == False, "Zero não é um número positivo."
print("Exercício 2 está correto.")

"""### exercicio 3

Escreva uma **definição de função** chamada ***is_negative*** que **recebe um número** e **retorna** **Verdadeiro** ou **Falso** se esse número **for negativo**.
"""

def is_negative(number):
   return True if number < 0 else False

assert is_negative(impar_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(par_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(impar_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(par_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_negative(0) == False, "Zero não é um número negativo."
print("Exercício 3 está correto.")

"""### exercicio 4

Escreva uma **definição de função** chamada ***is_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for ímpar**.
"""

def is_odd(number):
   if number%2 !=0:
      return True
   else:
      return False


assert is_odd(impar_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(par_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(impar_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_odd(par_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 4 está correto.")

"""### exercicio 5

Escreva uma definição de **função** chamada ***is_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se esse **número for par**.
"""

def is_even(number):
   if number%2 == 0:
      return True
   else:
      return False

assert is_even(2) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(impar_positivo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(par_positivo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(impar_negativo) == False, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert is_even(par_negativo) == True, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 5 está correto.")

"""### exercicio 6

Escreva uma definição de **função** chamada ***identity*** que **recebe qualquer argumento** e **retorna o valor** desse argumento. Não pense demais nisso!
"""

def identity(anything):
   return anything

assert identity(impar_positivo) == impar_positivo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(par_positivo) == par_positivo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(impar_negativo) == impar_negativo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
assert identity(par_negativo) == par_negativo, "Certifique-se de que a função está definida, nomeada corretamente e retorna o valor correto"
print("Exercício 6 está correto.")

"""### exercicio 7

Escreva uma definição de **função** chamada ***is_positive_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **maior que zero** e **ímpar**
"""

def is_positive_odd(number):
   if number > 0 and number%2 != 0:
      return True
   else:
      return False

assert is_positive_odd(3) == True, "Verifique sua sintaxe e lógica"
assert is_positive_odd(impar_positivo) == True, "Verifique sua sintaxe e lógica"
assert is_positive_odd(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_odd(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_odd(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 7 está correto.")

"""### exercicio 8

Escreva uma definição de **função** chamada ***is_positive_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **maior que zero** e **par**
"""

def is_positive_even(number):
   if number > 0 and number%2 == 0:
      return True
   else:
      return False

assert is_positive_even(4) == True, "Verifique sua sintaxe e lógica"
assert is_positive_even(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_even(par_positivo) == True, "Verifique sua sintaxe e lógica"
assert is_positive_even(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_positive_even(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 8 está correto.")

"""### exercicio 9

Escreva uma definição de **função** chamada ***is_negative_odd*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **menor que zero** e **ímpar**.
"""

def is_negative_odd(number):
   if number < 0 and number%2 != 0:
      return True
   else:
      return False

assert is_negative_odd(-3) == True, "Verifique sua sintaxe e lógica"
assert is_negative_odd(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_odd(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_odd(impar_negativo) == True, "Verifique sua sintaxe e lógica"
assert is_negative_odd(par_negativo) == False, "Verifique sua sintaxe e lógica"
print("Exercício 9 está correto.")

"""### exercicio 10

Escreva uma definição de **função** chamada ***is_negative_even*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o valor for **menor que zero** e **par**.
"""

def is_negative_even(number):
   if number < 0 and number%2 == 0:
      return True
   else:
      return False

assert is_negative_even(-4) == True, "Verifique sua sintaxe e lógica"
assert is_negative_even(impar_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(par_positivo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(impar_negativo) == False, "Verifique sua sintaxe e lógica"
assert is_negative_even(par_negativo) == True, "Verifique sua sintaxe e lógica"
print("Exercício 10 está correto.")

"""### exercicio 11

Escreva uma definição de **função** chamada ***half*** que **recebe um número** e **retorna a metade** do número fornecido.
"""

def half(number):
   return number/2

assert half(4) == 2
assert half(-5) == -2.5
assert half(impar_positivo) == impar_positivo / 2
assert half(par_positivo) == par_positivo / 2
assert half(impar_negativo) == impar_negativo / 2
assert half(par_negativo) == par_negativo / 2
print("Exercício 11 está correto.")

"""### exercicio 12

Escreva uma definição de **função** chamada ***double*** que **recebe um número** e **retorna o dobro** do número fornecido.
"""

def double(number):
   return number*2

assert double(4) == 8
assert double(-5) == -10
assert double(impar_positivo) == impar_positivo * 2
assert double(par_positivo) == par_positivo * 2
assert double(impar_negativo) == impar_negativo * 2
assert double(par_negativo) == par_negativo * 2
print("Exercício 12 está correto.")

"""### exercicio 13

Escreva uma definição de **função** chamada ***triple*** que **recebe um número** e **retorna o triplo** do número fornecido.
"""

def triple(number):
   return number*3

assert triple(4) == 12
assert triple(-5) == -15
assert triple(impar_positivo) == impar_positivo * 3
assert triple(par_positivo) == par_positivo * 3
assert triple(impar_negativo) == impar_negativo * 3
assert triple(par_negativo) == par_negativo * 3
print("Exercício 13 está correto.")

"""### exercicio 14

Escreva uma definição de **função** chamada ***reverse_sign*** que **recebe um número** e **retorna o número** fornecido, mas **com o sinal revertido**.
"""

def reverse_sign(number):
   return number*-1

assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(impar_positivo) == impar_positivo * -1
assert reverse_sign(par_positivo) == par_positivo * -1
assert reverse_sign(impar_negativo) == impar_negativo * -1
assert reverse_sign(par_negativo) == par_negativo * -1
print("Exercício 14 está correto.")

"""### exercicio 15

Escreva uma definição de **função** chamada ***absolute_value*** que **recebe um número** e **retorna o valor absoluto** do número fornecido
"""

def absolute_value(number):
   if number > 0:
      return number
   else:
      return number*-1

assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(impar_positivo) == impar_positivo
assert absolute_value(par_positivo) == par_positivo
assert absolute_value(impar_negativo) == impar_negativo * -1
assert absolute_value(par_negativo) == par_negativo * -1
print("Exercício 15 está correto.")

"""### exercicio 16

Escreva uma definição de **função** chamada ***is_multiple_of_three*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível por três**.
"""

## O nome era pra ser is_multiple_of_three, mas a correção automática corrigia com o nome de Fizz.

def Fizz(number):
   if number%3 == 0:
      return True
   else:
      return False

assert Fizz(3) == True
assert Fizz(15) == True
assert Fizz(9) == True
assert Fizz(4) == False
assert Fizz(10) == False
print("Exercício 16 está correto.")

"""### exercicio 17

Escreva uma definição de **função** chamada ***is_multiple_of_five*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível por cinco**.
"""

## O nome era pra ser is_multiple_of_five, mas a correção automática corrigia com o nome de Buzz.

def Buzz(number):
   if number%5== 0:
      return True
   else:
      return False

assert Buzz(3) == False
assert Buzz(15) == True
assert Buzz(9) == False
assert Buzz(4) == False
assert Buzz(10) == True
print("Exercício 17 está correto.")

"""### exercicio 18

Escreva uma definição de **função** chamada ***FizzBuzz*** que **recebe um número** e **retorna Verdadeiro** ou **Falso** se o número for **divisível** tanto por **três** quanto por **cinco**.
"""

def FizzBuzz(number):
   if number%3 == 0 and number%5 ==0:
      return True
   else:
      return False

assert FizzBuzz(15) == True
assert FizzBuzz(45) == True
assert FizzBuzz(3) == False
assert FizzBuzz(9) == False
assert FizzBuzz(4) == False
print("Exercício 18 está correto.")

"""### exercicio 19

Escreva uma definição de **função** chamada **square** que **recebe um número** e retorna o número **multiplicado** por **si mesmo**.
"""

def square(number):
   return number **2

assert square(3) == 9
assert square(2) == 4
assert square(9) == 81
assert square(impar_positivo) == impar_positivo * impar_positivo
print("Exercício 19 está correto.")

"""### exercicio 20

Escreva uma definição de **função** chamada ***add*** que **recebe dois números** e **retorna a soma**.
"""

def add(number, otherNumber):
   return number + otherNumber

assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercício 20 está correto.")

"""### exercicio 21

Escreva uma definição de **função** chamada ***cube*** que **recebe um número** e **retorna** o número **multiplicado** por **si mesmo**, **multiplicado** por **si mesmo**.
"""

def cube(number):
   return number **3

assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(impar_positivo) == impar_positivo * impar_positivo * impar_positivo
print("Exercício 21 está correto.")

"""### exercicio 22

Escreva uma definição de **função** chamada ***square_root*** que **recebe um número** e **retorna a raiz quadrada** do número fornecido
"""

def square_root(number):
   return number**0.5

assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercício 22 está correto.")

"""### exercicio 23

Escreva uma definição de **função** chamada ***subtract*** que **recebe dois números** e retorna o primeiro número menos o segundo argumento.
"""

def subtract(number, otherNumber):
   return number - otherNumber

assert subtract(8, 6) == 2
assert subtract(27, 4) == 23
assert subtract(12, 2) == 10
print("Exercício 23 está correto.")

"""### exercicio 24

Escreva uma definição de **função** chamada ***multiply*** que **recebe dois números** e retorna o **primeiro** número **multiplicado** pelo **segundo** argumento.
"""

def multiply(number, otherNumber):
   return number * otherNumber

assert multiply(2, 1) == 2
assert multiply(3, 5) == 15
assert multiply(5, 2) == 10
print("Exercício 24 está correto.")

"""### exercicio 25

Escreva uma definição de **função** chamada ***divide*** que **recebe dois números** e retorna o **primeiro** argumento **dividido** pelo **segundo** argumento.
"""

def divide(number, otherNumber):
   return number / otherNumber

assert divide(27, 9) == 3
assert divide(15, 3) == 5
assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
print("Exercício 25 está correto.")

"""### exercicio 26

Escreva uma definição de **função** chamada **quotient** que **recebe dois números** e retorna **apenas** o **quociente da divisão** do primeiro argumento pelo segundo argumento.
"""

def quotient(number, otherNumber):
   return number // otherNumber

assert quotient(27, 9) == 3
assert quotient(5, 2) == 2
assert quotient(10, 3) == 3
print("Exercício 26 está correto")

"""### exercicio 27

Escreva uma definição de **função** chamada ***remainder*** que **recebe dois números** e retorna o **resto da divisão** do **primeiro** argumento pelo **segundo** argumento.
"""

def remainder(number, otherNumber):
   return number % otherNumber

assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercício 27 está correto.")

"""### exercicio 28

Escreva uma definição de **função** chamada ***sum_of_squares*** que **recebe dois números**, **eleva cada número ao quadrado** e depois **retorna a soma** dos dois quadrados.
"""

def sum_of_squares(number, otherNumber):
   return number**2 + otherNumber**2


assert sum_of_squares(3, 2) == 13
assert sum_of_squares(5, 2) == 29
assert sum_of_squares(2, 4) == 20
print("Exercício 28 está correto.")

"""### exercicio 29

Escreva uma definição de **função** chamada ***times_two_plus_three*** que **recebe um número**, **multiplica-o por dois**, **adiciona 3** e retorna o resultado.
"""

def times_two_plus_three(number):
   return number*2+3

assert times_two_plus_three(0) == 3
assert times_two_plus_three(1) == 5
assert times_two_plus_three(2) == 7
assert times_two_plus_three(3) == 9
assert times_two_plus_three(5) == 13
print("Exercício 29 está correto.")


"""## Funções e laços aplicadas a listas

### Exercício 1
"""

# ## Aplicando funções a listas

# Exercício 1)
  # a) Escreva a definição de função chamada obter_maior_numero que recebe uma sequência de números e retorna o maior número.

def obter_maior_numero(sequence):
   return max(sequence)

assert obter_maior_numero([1, 2, 3]) == 3
assert obter_maior_numero([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 5
assert obter_maior_numero([-5, -3, 1]) == 1
print("Exercício 1a) está correto.")

"""### Exercício 1 b)"""

# b) Escreva a definição de função chamada obter_menor_numero que recebe uma sequência de números e retorna o menor número.

def obter_menor_numero(sequence):
   return min(sequence)

assert obter_menor_numero([1, 3, 2]) == 1
assert obter_menor_numero([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert obter_menor_numero([-4, -3, 1]) == -4
print("Exercício 1b) está correto.")

"""### Exercício 1 c)"""

# c) Escreva a definição de função chamada apenas_números_ímpares que recebe uma sequência de números e retorna os números ímpares em uma lista.

def apenas_números_ímpares(sequence):
   return [impar for impar in sequence if impar%2!=0]

assert apenas_números_ímpares([1, 2, 3]) == [1, 3]
assert apenas_números_ímpares([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert apenas_números_ímpares([-4, -3, 1]) == [-3, 1]
assert apenas_números_ímpares([2, 2, 2, 2, 2]) == []
print("Exercício 1c) está correto.")

"""### Exercício 1 d)"""

# Escreva a definição de função chamada apenas_números_pares que recebe uma sequência de números e retorna os números pares em uma lista.

def apenas_números_pares(sequence):
   return [par for par in sequence if par%2==0]

assert apenas_números_pares([1, 2, 3]) == [2]
assert apenas_números_pares([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert apenas_números_pares([-4, -3, 1]) == [-4]
assert apenas_números_pares([1, 1, 1, 1, 1, 1]) == []
print("Exercício 1d) está correto.")

"""### Exercício 2 a)"""

# Exercício 2)
# a) Escreva a definição de função chamada apenas_números_positivos que recebe uma sequência de números e retorna os números positivos em uma lista.
def apenas_números_positivos(sequencia):
  num_positivo = [numero for numero in sequencia  if numero> 0]
  return num_positivo

assert apenas_números_positivos([1, 2, 3]) == [1, 2, 3]
assert apenas_números_positivos([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert apenas_números_positivos([-4, -3, 1]) == [1]
print("Exercício 2a) está correto.")

"""### Exercício 2 b)"""

# b) Escreva a definição de função chamada apenas_números_negativos que recebe uma sequência de números e retorna os números negativos em uma lista.
def apenas_números_negativos(sequencia):
  num_negativo = [numero for numero in sequencia  if numero < 0]
  return num_negativo

assert apenas_números_negativos([1, 2, 3]) == []
assert apenas_números_negativos([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert apenas_números_negativos([-4, -3, 1]) == [-4, -3]
print("Exercício 2b) está correto.")


"""### Exercício 3 a)"""

# a) Escreva a definição de função chamada contar_pares que recebe uma sequência de números e retorna o número de números pares.

def contar_pares(sequencia):
    contador = 0

    for numero in sequencia:
        if numero % 2 == 0:
            contador += 1

    return contador

assert contar_pares([1, 2, 3]) == 1
assert contar_pares([2, 5, 6]) == 2
assert contar_pares([3, 3, 3]) == 0
assert contar_pares([5, 6, 7, 8] ) == 2
print("Exercício 3a) está correto.")

"""### Exercício 3 b)"""

# b) Escreva a definição de função chamada tem_ímpares que recebe uma sequência de números e retorna True se houver algum número ímpar na sequência.

def tem_ímpares(sequence):
    contador = 0

    for numero in sequence:
        if numero % 2 != 0:
            contador += 1

    if contador != 0:
       return True
    else:
       return False
assert tem_ímpares([1, 2, 3]) == True
assert tem_ímpares([2, 5, 6]) == True
assert tem_ímpares([3, 3, 3]) == True
assert tem_ímpares([2, 4, 6]) == False
print("Exercício 3c) está correto.")
