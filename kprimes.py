#!/usr/bin/env python
# -*- coding: utf-8 -*-


# print(isprime(1291)) # Verifica se um número é primo
# print(quantprimes(-4, 100000)) # Retorna a quantidade de primos em um intervalo
# print(keyprime(97)) # Retorna a posição de um número primo no conjunto dos naturais
# print(randprime(0, 100)) # Retorna um número primo aleatório dentro de um intervalo
# print(previousprime(100)) # Retorna o número primo anterior
# print(nextprime(23)) # Retorna o próximo número primo


from typing import Union


def kprimes(comeco_intervalo: int, fim_intervalo: int, previous: bool=False, next_prime: bool=False, retornar: int=0):

    primo: bool = True

    if comeco_intervalo <= 2:
        primos_no_intervalo: dict = {1: 2}
        quant_primos = len(primos_no_intervalo)
        comeco_intervalo = 3
    else:
        primos_no_intervalo = {1: 2, 2: 3}
        quant_primos = len(primos_no_intervalo)
        for numero_analisado in range(5, comeco_intervalo + 1, 2):
            raiz_quadrada_numero_analisado = numero_analisado ** .5
            for candidato_a_divisor in primos_no_intervalo.values():
                if candidato_a_divisor > raiz_quadrada_numero_analisado:
                    break
                if numero_analisado % candidato_a_divisor == 0:
                    primo = False
                    break
            if primo:
                quant_primos += 1
                primos_no_intervalo[quant_primos] = numero_analisado
            primo = True

    quant_para_ignorar = len(primos_no_intervalo)

    if comeco_intervalo % 2 == 0:
        comeco_intervalo += 1
    for numero_analisado in range(comeco_intervalo, fim_intervalo + 1, 2):
        raiz_quadrada_numero_analisado = numero_analisado ** .5
        for candidato_a_divisor in primos_no_intervalo.values():
            if candidato_a_divisor > raiz_quadrada_numero_analisado:
                break
            if numero_analisado % candidato_a_divisor == 0:
                primo = False
                break
        if primo:
            quant_primos += 1
            primos_no_intervalo[quant_primos] = numero_analisado
        primo = True

    if previous:
        return primos_no_intervalo[quant_primos - 1]

    if next_prime:
        numero_analisado = fim_intervalo
        if numero_analisado >= 2:
            while True:
                numero_analisado += 1
                raiz_quadrada_numero_analisado = numero_analisado ** .5
                for candidato_a_divisor in primos_no_intervalo.values():
                    if candidato_a_divisor > raiz_quadrada_numero_analisado:
                        break
                    if numero_analisado % candidato_a_divisor == 0:
                        primo = False
                        break
                if primo:
                    quant_primos += 1
                    primos_no_intervalo[quant_primos] = numero_analisado
                    break
                primo = True
        return primos_no_intervalo[quant_primos]

    if retornar == 0:
        return primos_no_intervalo, quant_para_ignorar, quant_primos
    elif retornar == 1:
        return primos_no_intervalo
    elif retornar == 3:
        return quant_primos, quant_para_ignorar


def isprime(numero: int) -> bool:

    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return False

    isprimo = None

    primos_no_intervalo = kprimes(0, numero, retornar=1)

    for v in primos_no_intervalo.values():
        if numero == v:
            isprimo = True
            break
        else:
            isprimo = False

    return isprimo


def keyprime(numero: int) -> Union[int, None]:

    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return None

    if not isprime(numero):
        return None

    keyprimo = None

    primos_no_intervalo = kprimes(0, numero, retornar=1)

    for k, v in primos_no_intervalo.items():
        if numero == v:
            keyprimo = k
            break

    return keyprimo


def quantprimes(comeco_intervalo: int, fim_intervalo: int) -> int:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo >= fim_intervalo:
        raise ValueError
    if fim_intervalo < 2:
        return 0

    quant_primos, quant_para_ignorar = kprimes(comeco_intervalo, fim_intervalo, retornar=3)

    if comeco_intervalo <= 2:
        return quant_primos
    else:
        return quant_primos - quant_para_ignorar


def randprime(comeco_intervalo: int, fim_intervalo: int) -> Union[int, None]:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo >= fim_intervalo:
        raise ValueError
    if fim_intervalo < 2:
        return None

    primos_no_intervalo, quant_para_ignorar, quant_primos = kprimes(comeco_intervalo, fim_intervalo)

    if quant_primos - quant_para_ignorar == 0:
        return None

    list_keys: list = []

    for k in primos_no_intervalo.keys():
        list_keys.append(k)
    from random import randint
    prime_random: int = randint(list_keys[quant_para_ignorar], quant_primos)

    return primos_no_intervalo[prime_random]


def previousprime(numero: int) -> Union[int, None]:

    if not isinstance(numero, int):
        raise TypeError
    if numero <= 2:
        return None

    return kprimes(2, numero, previous=True)


def nextprime(numero: int) -> int:

    if not isinstance(numero, int):
        raise TypeError

    return kprimes(2, numero, next_prime=True)
