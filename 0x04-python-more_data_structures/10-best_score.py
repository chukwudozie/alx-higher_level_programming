#!/usr/bin/python3
def best_score(a_dictionary):
	if not a_dictionary:
		return None
	key_list = list(a_dictionary.keys())
	max_val = max(a_dictionary.values())
	max_pos = list(a_dictionary.values()).index(max_val)
	return key_list[max_pos]

