#!/usr/bin/env python
# -*- coding: utf-8 -*-


# print(isprime(1291)) # Verifica se um número é primo
# print(quantprimes(-4, 100000)) # Retorna a quantidade de primos em um intervalo
# print(keyprime(97)) # Retorna a posição de um número primo no conjunto dos naturais
# print(randprime(0, 100)) # Retorna um número primo aleatório dentro de um intervalo
# print(previousprime(100)) # Retorna o número primo anterior
# print(nextprime(23)) # Retorna o próximo número primo


from typing import Union


def kprimes(comeco_intervalo: int, fim_intervalo: int, /, *, next_prime: bool = False):

    primo: bool = True

    if comeco_intervalo <= 2:
        primos_no_intervalo: dict = {1: 2}
        yield 2
        quant_primos = 1
        comeco_intervalo = 3
    else:
        primos_no_intervalo = {1: 2, 2: 3}
        yield 2
        yield 3
        quant_primos = 2
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
                yield numero_analisado
                primos_no_intervalo[quant_primos] = numero_analisado
            primo = True

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
            yield numero_analisado
            primos_no_intervalo[quant_primos] = numero_analisado
        primo = True
    
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
                    yield numero_analisado
                    break
                primo = True


def isprime(numero: int, /) -> bool:

    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return False
    
    for i in kprimes(0, numero):
        if numero == i:
            return True
    
    return False


def keyprime(numero: int, /) -> Union[int, None]:

    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return None

    if not isprime(numero):
        return None
    
    p = 0
    
    for i in kprimes(0, numero):
        p += 1
        if numero == i:
            return p


def quantprimes(comeco_intervalo: int, fim_intervalo: int, /) -> int:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo >= fim_intervalo:
        raise ValueError
    if fim_intervalo < 2:
        return 0
        
    q = 0
    
    for i in kprimes(comeco_intervalo, fim_intervalo):
        if i >= comeco_intervalo:
            q += 1
    
    return q
    

def randprime(comeco_intervalo: int, fim_intervalo: int, /) -> Union[int, None]:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo >= fim_intervalo:
        raise ValueError
    if fim_intervalo < 2:
        return None
    
    x = quantprimes(comeco_intervalo, fim_intervalo)
    from random import randint
    y = randint(1, x)
    del(x)
    z = 0
    for i in kprimes(comeco_intervalo, fim_intervalo):
        if i >= comeco_intervalo:
            z += 1
            if z == y:
                return i


def previousprime(numero: int, /) -> Union[int, None]:

    if not isinstance(numero, int):
        raise TypeError
    if numero <= 2:
        return None
    
    x = 0
    y = 0
    z = 0
    
    a: int = quantprimes(2, numero)
    b: bool = a % 2 == 0
    del(a)
    
    for i in kprimes(2, numero):
        x += 1
        if x % 2 == 0:
            y = i
        else:
            z = i
    else:
        if numero > i:
            return i
    
    if b:
        if y == 0:
            return None
        return z
    return y


def nextprime(numero: int, /) -> int:

    if not isinstance(numero, int):
        raise TypeError
    
    for i in kprimes(2, numero, next_prime=True):
        pass
    else:
        return i
