#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from elevator import *
from sstf import *
from fcfs import *

def main():
    # Carrega o arquivo em uma lista
    lines = sys.stdin.readlines()

    sstf = SSTF(lines)
    fcfs = FCFS(lines)
    elevator = Elevator(lines)

    print('FCFS', fcfs.output)
    print('SSTF', sstf.output)
    print('ELEVADOR', elevator.output)

if __name__ == "__main__":
    main()
