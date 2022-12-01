import numpy as np


def process_input(path=None):

    with open(path, 'r') as input:
        data = input.read()

    input.close()

    data_list = data.rstrip('\n').split('\n\n')
    elf_list = [x.split('\n') for x in data_list]
    elf_cals = [[eval(i) for i in elf] for elf in elf_list]

    return elf_cals


def find_top_elves(pop=None, n=1):

    totals = [np.sum(x) for x in pop]

    args = np.argsort(totals)[::-1][:n]

    return [pop[x] for x in args]


def get_total_calories(pop=None):

    pop = [sum(x) for x in pop]

    return sum(pop)