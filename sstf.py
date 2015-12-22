#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, copy

class SSTF(object):

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

		# Valor da menor distancia escolhida para cada movimento do braco
		shortest_distance = 999
		# Posicao da menor distancia escolhida para cada movimento do braco
		best_position = 0
		for i in range(len(inputs)):
			# Distancia calculada para cada posicao requerida
			distance = math.trunc(math.fabs(current_cylinder - inputs[i]))

			# Verifica se a distancia atualmente calculada e menor que a distancia menor que ja se tem
			if  distance < shortest_distance:
				# Salva-se a menor distancia
				shortest_distance = distance
				# Salva-se a posicao da menor distancia
				best_position = i

		# E somado a distancia ao cilindro mais proximo
		self.output += shortest_distance

		# Posicao atual escolhida
		current_position = inputs.pop(best_position)

		while len(inputs) > 0:
			# Menor distancia e reiniciada para buscar a proxima menor distancia
			shortest_distance = 999

			for i in range(len(inputs)):
				# Distancia calculada para cada posicao requerida
				distance = math.trunc(math.fabs(current_position - inputs[i]))

				# Verifica se a distancia atualmente calculada e menor que a distancia menor que ja se tem
				if distance < shortest_distance:
					# Salva-se a menor distancia
					shortest_distance = distance
					# Salva-se a posicao da menor distancia
					best_position = i

			# E somado a distancia ao cilindro mais proximo
			self.output += shortest_distance

			# Posicao atual escolhida
			current_position = inputs.pop(best_position)
