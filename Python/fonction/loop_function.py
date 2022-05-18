#!/usr/bin/env python3

from ctypes.wintypes import CHAR
import string
import sys
from typing import List
sys.path.append('./')
from . import add, sub, pow, div, modulo, squared, str_concat
def loop_function(funct,repeat,*args):
    if repeat < 0:
        return "erreur"
    if repeat == 0:
        return determineTypeResult(args[0])
    functione = {
        "add" : add.add,
        "sub" : sub.sub,
        "pow" : pow.pow,
        "div" : div.div,
        "modulo" : modulo.modulo,
        "squared" : squared.squared,
        "str_concat" : str_concat.str_concat
    }
    for _ in range(repeat):
        as_list = list(args)
        as_list[0] = functione[funct](*as_list)
    
    return determineTypeResult(as_list[0])

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