import numpy as np
import string

### DAY 1 FUNCTIONS
def process_day1_input(path=None):

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

### DAY 2 FUNCTIONS
def process_day2_input(path=None):
    with open(path, 'r') as input:
        data = input.read()

    input.close()

    rounds = [(x.split()[0], x.split()[1]) for x in data.rstrip('\n').split('\n')]

    return rounds

choice_score = {
    'rock': 1,
    'paper': 2,
    'scissor': 3
}

choice_lookup = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissor',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissor'
}

round_outcomes = {
    ('rock','paper'): 'win',
    ('rock','scissor'): 'lose',
    ('rock', 'rock'): 'draw',
    ('paper', 'paper'): 'draw',
    ('paper', 'rock'): 'lose',
    ('paper', 'scissor'): 'win',
    ('scissor', 'paper'): 'lose',
    ('scissor','scissor'): 'draw',
    ('scissor', 'rock'): 'win'
}

outcome_to_score = {
    'win': 6,
    'lose': 0,
    'draw': 3
}

def score_round(choices=None):

    my_score = 0

    # convert choice to name
    their_choice, my_choice = choices

    their_choice_nm = choice_lookup.get(their_choice)
    my_choice_nm = choice_lookup.get(my_choice)

    # get score for my choice in index 1
    round_choice_score = choice_score.get(my_choice_nm)
    my_score += round_choice_score

    # score for outcome
    round_score = outcome_to_score.get(round_outcomes.get((their_choice_nm, my_choice_nm)))
    my_score += round_score

    return my_score


def get_my_score(rounds=None):
    scores = [score_round(x) for x in rounds]

    return np.sum(scores)

strategy_lookup = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

choice_lookup_reversed = {
    'rock': 'X',
    'paper': 'Y',
    'scissor': 'Z'
}

get_right_choice = {
    ('rock','win'): 'paper',
    ('rock','lose'): 'scissor',
    ('rock', 'draw'): 'rock',
    ('paper', 'win'): 'scissor',
    ('paper', 'lose'): 'rock',
    ('paper', 'draw'): 'paper',
    ('scissor', 'win'): 'rock',
    ('scissor','lose'): 'paper',
    ('scissor', 'draw'): 'scissor'
}

def create_new_choices(strategy_choice=None):

    their_choice, desired_outcome = strategy_choice

    their_choice_nm = choice_lookup.get(their_choice)
    desired_outcome_nm = strategy_lookup.get(desired_outcome)

    my_choice = get_right_choice.get((their_choice_nm, desired_outcome_nm))
    my_choice_ltr = choice_lookup_reversed.get(my_choice)

    return (their_choice, my_choice_ltr)


### Day 3

def read_day3_input(path=None):
    with open(path, 'r') as input:
        supplies = input.read()

    supplies = supplies.rstrip('\n').split('\n')

    return supplies

def supplies_in_pockets(cargo=None):

    cargo_list = [x for x in cargo]
    split_point = int(len(cargo_list)/2)

    pocket1 = cargo_list[:split_point]
    pocket2 = cargo_list[split_point:]

    assert len(pocket1) == len(pocket2), 'Supplies Not Split Evenly'
    return pocket1, pocket2

def compare_pockets(pocket1=None, pocket2=None):

    pocket1 = set(pocket1)
    pocket2 = set(pocket2)

    return set(pocket1).intersection(set(pocket2))

def determine_badge_from_cargo(inputs=None):

    input_lists = [[x for x in backpack] for backpack in inputs]

    sets = map(set, input_lists)
    return set.intersection(*sets)


def create_priority_lookup_dict():

    item_priority_lookup = {}

    for i, char in enumerate(string.ascii_lowercase):
        item_priority_lookup[char] = i+1

    for i, char in enumerate(string.ascii_uppercase):
        item_priority_lookup[char] = i+27

    return item_priority_lookup


def get_priority_score(overlap=None, lookup_dict=None):

    priorities = [lookup_dict.get(x) for x in overlap]

    return sum(priorities)

def analyze_packpack(cargo=None):

    pocket1, pocket2 = supplies_in_pockets(cargo=cargo)
    overlap = compare_pockets(pocket1=pocket1, pocket2=pocket2)

    # Not most efficient to recreate throughout loop but it's fine for this
    priority_lookup_dict = create_priority_lookup_dict()
    score = get_priority_score(overlap=overlap, lookup_dict=priority_lookup_dict)

    return score


def get_badge_priority_score(group=None):

    badge = determine_badge_from_cargo(inputs=group)
    # Not most efficient to recreate throughout loop but it's fine for this
    priority_lookup_dict = create_priority_lookup_dict()
    score = get_priority_score(overlap=badge, lookup_dict=priority_lookup_dict)

    return score


def create_elf_groups(supplies=None, chunksize=3):

    chunks = [x for x in zip(*(iter(supplies),) * chunksize)]

    return chunks


### Day 4

def get_day4_input(path=None):
    with open(path, 'r') as input:
        assignments = input.read()

    input.close()
    assignments = assignments.rstrip().split('\n')

    return assignments

def is_assignment_subset(assignments=None):

    ass1, ass2 = assignments.split(',')

    ass1 = ass1.split('-')
    ass2 = ass2.split('-')

    ass1_set = set(x for x in range(int(ass1[0]), int(ass1[1])+1))
    ass2_set = set(x for x in range(int(ass2[0]), int(ass2[1])+1))

    return (ass1_set.issubset(ass2_set) or ass2_set.issubset(ass1_set))


def do_assignments_overlap(assignments=None):

    ass1, ass2 = assignments.split(',')

    ass1 = ass1.split('-')
    ass2 = ass2.split('-')

    ass1_set = set(x for x in range(int(ass1[0]), int(ass1[1])+1))
    ass2_set = set(x for x in range(int(ass2[0]), int(ass2[1])+1))

    inter = ass1_set.intersection(ass2_set)

    return len(inter) > 0