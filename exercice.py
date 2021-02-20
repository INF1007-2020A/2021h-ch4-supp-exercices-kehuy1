#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	if len(string) % 2 == 0:
		return True
	else:
		return False


def get_num_char(string, char):
	num = 0
	for i in string:
		if i == char:
			num += 1
	return num


def get_first_part_of_name(name):
	string = name
	for i in range(len(name)):
		if string[i] == chr(ord('-')):
			name = string[:i].capitalize()
	return f"Bonjour, {name}"


def get_random_sentence(animals, adjectives, fruits):
	animals = random.choice(animals)
	adjectives = random.choice(adjectives)
	fruits = random.choice(fruits)
	return f'Aujourd’hui, j’ai vu un {animals} s’emparer d’un panier {adjectives} plein de {fruits}.'


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
