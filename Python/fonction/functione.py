#!/usr/bin/env python3

def functione(key : str):
	import fonction.add as add, fonction.sub as sub, fonction.pow as pow, fonction.div as div, fonction.modulo as modulo, fonction.squared as squared, fonction.str_concat as str_concat, fonction.mul as mul, fonction.hello_world as hello_world

	table = {
	"add" : add.add,
	"sub" : sub.sub,
	"pow" : pow.pow,
	"div" : div.div,
	"modulo" : modulo.modulo,
	"squared" : squared.squared,
	"str_concat" : str_concat.str_concat,
	"mul" : mul.mul,
	"hello_world" : hello_world.hello_world,
	}
	return table[key]

if __name__ == '__main__':
	print(functione("add")(1,2))
	print(functione("sub")(1,2))
	print(functione("pow")(1,2))
	print(functione("div")(1,2))
	print(functione("modulo")(1,2))
	print(functione("squared")(2))
	print(functione("str_concat")(1,2))
	print(functione("mul")(1,2))
	print(functione("hello_world")())