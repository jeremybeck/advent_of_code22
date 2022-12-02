from advent_of_code.src.aoc22 import *

def day1_star1():
    elf_cals = process_day1_input(path='../inputs/day1_input.txt')
    return get_total_calories(pop=find_top_elves(pop=elf_cals, n=1))

def day1_star2():
    elf_cals = process_day1_input(path='../inputs/day1_input.txt')
    return get_total_calories(pop=find_top_elves(pop=elf_cals, n=3))

def day2_star1():
    rounds = process_day2_input(path='../inputs/day2_input.txt')
    return get_my_score(rounds=rounds)

def day2_star2():
    rounds = process_day2_input(path='../inputs/day2_input.txt')
    rounds_corrected = [create_new_choices(x) for x in rounds]
    return get_my_score(rounds=rounds_corrected)