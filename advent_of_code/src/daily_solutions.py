from advent_of_code.src.aoc22 import *

def day1_star1():
    elf_cals = process_day1_input(path='../inputs/day1_input.txt')
    return get_total_calories(pop=find_top_elves(pop=elf_cals, n=1))

def day1_star2():
    elf_cals = process_day1_input(path='../inputs/day1_input.txt')
    return get_total_calories(pop=find_top_elves(pop=elf_cals, n=3))
