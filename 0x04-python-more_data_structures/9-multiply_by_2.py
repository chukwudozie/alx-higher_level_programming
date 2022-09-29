#!/usr/bin/python3
def multiply_by_2(a_dictionary):
	val = list(map(lambda x: 2 *x, a_dictionary.values()))
	return dict(zip(a_dictionary.keys(), val))

