#!/usr/bin/env python3

from fonction.functione import functione as fct
def loop_function(funct,repeat,*args):
    print(f"funct : {funct}, repeat : {repeat}, args : {args}")
    if repeat < 0:
        return "erreur"
    if repeat == 0:
        return args[0]

    as_list = list(args)
    for _ in range(repeat):
        as_list[0] = fct(funct)(*as_list)
        print(as_list[0])
    return as_list[0]

def determineTypeResult(result):
        if isinstance(result, list):
            return list(result)
        if isinstance(result, tuple):
            return tuple(result)
        if isinstance(result, int):
            return int(result)
        if isinstance(result, float):
            return float(result)
        if isinstance(result, str):
            return str(result)
        if isinstance(result, bool):
            return bool(result)
        if isinstance(result, complex):
            return complex(result)