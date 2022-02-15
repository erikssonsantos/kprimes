#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Funciona com python 3.8.0 ou versões superiores

# print(isprime(1291)) # Verifica se um número é primo
# print(quantprimes(-4, 100000)) # Retorna a quantidade de primos em um intervalo
# print(keyprime(97)) # Retorna a posição de um número primo na sequência geral
# print(randprime(0, 100)) # Retorna um número primo aleatório dentro de um intervalo
# print(previousprime(100)) # Retorna o número primo anterior
# print(nextprime(23)) # Retorna o próximo número primo


from typing import Union
from math import floor


def kprimes(comeco_intervalo: int, fim_intervalo: int, /, *, next_prime: bool = False):

    primo: bool = True
    primos_no_intervalo: dict = {}
    viavel: bool = True
    quant_primos: int = 0
    comeco_intervalo_2: int = comeco_intervalo
    
    if fim_intervalo < comeco_intervalo:
        viavel = False
        
    elif comeco_intervalo <= 2:
        primos_no_intervalo = {1: 2}
        yield 2
        quant_primos = 1
        comeco_intervalo_2 = 3
        
    elif comeco_intervalo == 3:
        primos_no_intervalo = {1: 2, 2: 3}
        yield 2
        yield 3
        quant_primos = 2
        comeco_intervalo_2 = 5
        
    elif comeco_intervalo == 4:
        primos_no_intervalo = {1: 2, 2: 3}
        yield 2
        yield 3
        quant_primos = 2
        comeco_intervalo_2 = 5
    
    elif comeco_intervalo == 5:
        primos_no_intervalo = {1: 2, 2: 3, 3: 5}
        yield 2
        yield 3
        yield 5
        quant_primos = 3
        comeco_intervalo_2 = 7
    
    elif comeco_intervalo == 6:
        primos_no_intervalo = {1: 2, 2: 3, 3: 5}
        yield 2
        yield 3
        yield 5
        quant_primos = 3
        comeco_intervalo_2 = 7
    
    else:
        primos_no_intervalo = {1: 2, 2: 3, 3: 5}
        yield 2
        yield 3
        yield 5
        quant_primos = 3
        
        pulo = 0
        
        limite_de_teste = floor(comeco_intervalo_2 ** .5)
        testadores = list(primos_no_intervalo.values())[:limite_de_teste]
        len_testadores = len(testadores)
        for numero_analisado in range(7, comeco_intervalo + 1, 2):
            pulo += 1
            if pulo == 5:
                pulo = 0
                continue
            limite_de_teste = floor(numero_analisado ** .5)
            for candidato_a_divisor in testadores:
                if candidato_a_divisor > limite_de_teste:
                    break
                if numero_analisado % candidato_a_divisor == 0:
                    primo = False
                    break
            if primo:
                quant_primos += 1
                yield numero_analisado
                primos_no_intervalo[quant_primos] = numero_analisado
                if limite_de_teste > primos_no_intervalo[len_testadores + 1] or len_testadores < limite_de_teste:
                    testadores.append(primos_no_intervalo[len_testadores + 1])
                    len_testadores += 1
            primo = True
            
        
        if comeco_intervalo % 2 == 0:
            comeco_intervalo_2 = comeco_intervalo + 1
    
    
    if viavel:
        
        pulo = None
        
        ultimo_digito = int(str(comeco_intervalo_2)[-1])
        
        if ultimo_digito == 7:
            pulo = 0
        elif ultimo_digito == 9:
            pulo = 1
        elif ultimo_digito == 1:
            pulo = 2
        elif ultimo_digito == 3:
            pulo = 3
        elif ultimo_digito == 5:
            pulo = 4
        
        limite_de_teste = floor(comeco_intervalo_2 ** .5)
        testadores = list(primos_no_intervalo.values())[:limite_de_teste]
        len_testadores = len(testadores)
        for numero_analisado in range(comeco_intervalo_2, fim_intervalo + 1, 2):
            pulo += 1
            if pulo == 5:
                pulo = 0
                if numero_analisado != 5:
                    continue
            limite_de_teste = floor(numero_analisado ** .5)
            for candidato_a_divisor in testadores:
                if candidato_a_divisor > limite_de_teste:
                    break
                if numero_analisado % candidato_a_divisor == 0:
                    primo = False
                    break
            if primo:
                quant_primos += 1
                yield numero_analisado
                primos_no_intervalo[quant_primos] = numero_analisado
                if limite_de_teste > primos_no_intervalo[len_testadores + 1] or len_testadores < limite_de_teste:
                    testadores.append(primos_no_intervalo[len_testadores + 1])
                    len_testadores += 1
            primo = True
            
        
        if next_prime:
            numero_analisado = fim_intervalo
            
            if numero_analisado >= 2:

                if numero_analisado == 2:
                    quant_primos += 1
                    primos_no_intervalo[quant_primos] = 3
                    yield 3
                elif numero_analisado in (3, 4):
                    quant_primos += 1
                    primos_no_intervalo[quant_primos] = 5
                    yield 5
                elif numero_analisado in (5, 6):
                    quant_primos += 1
                    primos_no_intervalo[quant_primos] = 7
                    yield 7
                else:
                    
                    if numero_analisado % 2 == 0:
                        numero_analisado += 1
                    if numero_analisado in primos_no_intervalo.values():
                        numero_analisado += 2
                    
                    ultimo_digito = int(str(numero_analisado)[-1])
            
                    if ultimo_digito == 7:
                        pulo = 0
                    elif ultimo_digito == 9:
                        pulo = 1
                    elif ultimo_digito == 1:
                        pulo = 2
                    elif ultimo_digito == 3:
                        pulo = 3
                    elif ultimo_digito == 5:
                        pulo = 4
                    
                    limite_de_teste = floor(numero_analisado ** .5)
                    testadores = list(primos_no_intervalo.values())[:limite_de_teste]
                    len_testadores = len(testadores)
                    while True:
                        pulo += 1
                        if pulo == 5:
                            pulo = 0
                            continue
                        limite_de_teste = floor(numero_analisado ** .5)
                        for candidato_a_divisor in testadores:
                            if candidato_a_divisor > limite_de_teste:
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
                        numero_analisado += 2


def verificacao_preliminar(numero: int, /) ->bool:
    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return False
    if numero % 2 == 0:
        return False
    if numero % 5 == 0 and numero > 5:
        return False
    
    return True


def isprime_core(numero: int, /) -> bool:
    
    if numero in kprimes(0, numero):
        return True


def isprime(numero: int, /, *, preliminar_foi_feita: bool = False) -> bool:
    
    if preliminar_foi_feita:
        if isprime_core(numero):
            return True
    
    if verificacao_preliminar(numero):
        if isprime_core(numero):
            return True
    
    return False


def keyprime(numero: int, /) -> Union[int, None]:
    
    if verificacao_preliminar(numero):
        
        if not isprime(numero, preliminar_foi_feita=True):
            return None

        p = 0

        return tuple(kprimes(0, numero)).index(numero) + 1
        
    return None


def quantprimes(comeco_intervalo: int, fim_intervalo: int, /) -> int:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo > fim_intervalo:
        raise ValueError
    if fim_intervalo < 2:
        return 0

    q = 0

    if comeco_intervalo <= 2:
        for i in kprimes(comeco_intervalo, fim_intervalo):
                q += 1
    else:
        for i in kprimes(comeco_intervalo, fim_intervalo):
            if i >= comeco_intervalo:
                q += 1

    return q


def randprime(comeco_intervalo: int, fim_intervalo: int, /) -> Union[int, None]:

    if not isinstance(comeco_intervalo, int) or not isinstance(fim_intervalo, int):
        raise TypeError
    if comeco_intervalo > fim_intervalo:
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

    x: int = 0
    y: int = 0
    z: int = 0

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
    
    return tuple(kprimes(2, numero, next_prime=True))[-1]
