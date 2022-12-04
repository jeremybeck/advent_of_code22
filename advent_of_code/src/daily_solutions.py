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

def day3_star1():
    supplies = read_day3_input(path='../inputs/day3_inputs.txt')
    return sum([analyze_packpack(cargo=x) for x in supplies])

def day3_star2():
    supplies = read_day3_input(path='../inputs/day3_inputs.txt')
    elf_groups = create_elf_groups(supplies=supplies, chunksize=3)
    return sum([get_badge_priority_score(group=x) for x in elf_groups])

def day4_star1():
    assignments = get_day4_input(path='../inputs/day4_input.txt')
    return sum([is_assignment_subset(assignments=x) for x in assignments])

def day4_star2():
    assignments = get_day4_input(path='../inputs/day4_input.txt')
    return sum([do_assignments_overlap(assignments=x) for x in assignments])