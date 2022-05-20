#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def multipletest(*args):
    if len(args) == 0:
        print("on ne peut avoir 0 argument pour les test")
    table=[]
    for a in args:
        if type(a) == float:
            table.append(int(a))
        else:
            table.append(a)
            
    return table
def keyRecupDic(*args):
	table = [key for key, val in args[0].items()]
	print(table)
	return table
def valueRecupDic(*args):
	table = [val for key, val in args[0].items()]
	print(table)
	return table
dictionaire={
	"a": "abricot",
	"b": "brouette",
}
keyRecupDic(dictionaire)
valueRecupDic(dictionaire)