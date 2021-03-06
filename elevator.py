#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class Elevator(object):

	def __init__(self, lines):
		# Copia de 'lines' para nao modificar o arquivo original
		inputs = copy.deepcopy(lines)

		# Valor com a quantidade total de cilidros percorridos
		self.output = 0

		# Converte todos os valores de entrada em inteiros
		for i,line in enumerate(inputs):
			inputs[i] = int(line.split()[0])

		# Posicao do ultimo cilindro do disco
		last_cylinder = inputs.pop(0)
		# Posicao do cilindro inicial
		current_cylinder = inputs.pop(0)

		# Ordena o vetor em ordem decrescente
		inputs.sort()
		inputs.reverse()

		# Calcula o primeiro deslocamento do braco do disco
		self.output += abs(current_cylinder - inputs[0])
		i = 0
		while i < len(inputs) - 1:
			# Calcula todos os outros deslocamentos do braco do disco
			self.output += abs(inputs[i] - inputs[i+1])
			i += 1
