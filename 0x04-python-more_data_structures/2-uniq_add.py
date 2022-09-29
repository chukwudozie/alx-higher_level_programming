#!/usr/bin/python3

def uniq_add(my_list=[]):
	"""
	Args:
		my_list: given list
	Returns:
		int: sum
	"""
	x = list(set(my_list))
	return sum(x)

