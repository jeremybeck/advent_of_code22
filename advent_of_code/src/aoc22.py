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