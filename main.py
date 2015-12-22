#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt
from elevator import *
from sstf import *
from fcfs import *

def main(argv):
    # Recebe o nome do arquivo de entrada
    inputfile = sys.argv[-1]

    if(inputfile == sys.argv[0]): # Verifica se algum arquivo foi recebido
        print('Arquivo nao pode ser lido!!')
    else:
        # Abre o arquivo
        arq = open(inputfile, 'r')
        # Carrega o arquivo em uma lista
        lines = arq.readlines()

        sstf = SSTF(lines)
        fcfs = FCFS(lines)
        elevator = Elevator(lines)

        print('FCFS', fcfs.output)
        print('SSTF', sstf.output)
        print('ELEVADOR', elevator.output)

        # Fecha o arquivo
        arq.close()

if __name__ == "__main__":
    main(sys.argv[1:])
