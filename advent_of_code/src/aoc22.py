import numpy as np
import string
import re

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


### Day 5


def process_cargo_stacks(stacks=None,test=False):

    stack_contents = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    if test:
        stack_map = [(i, stacks[-1].index(str(i))) for i in range(1,4)]
    else:
        stack_map = [(i, stacks[-1].index(str(i))) for i in range(1,10)]

    for row in stacks[:-1]:
        for stack, idx in stack_map:
            try:
                if row[idx] == ' ':
                    pass
                else:
                    stack_dict = stack_contents.get(stack)
                    stack_dict.insert(0,row[idx])
                    stack_contents[stack] = stack_dict
            except Exception as E:
                #print(E)

                pass

    return stack_contents


def split_cargo_manifest(manifest=None):

    for i, line in enumerate(manifest):
        if line.startswith(' 1   2   3'):
            idx = i

    stacks = manifest[0:idx+1]
    moves = manifest[idx+2:]

    return stacks, moves


def process_moves(moves):

    moves_processed = []

    for move in moves:
        move = move.split(' ')
        count = int(move[1])
        source = int(move[3])
        destination = int(move[5])

        moves_processed.append({'count':count, 'source':source, 'destination':destination})

    return moves_processed


def get_day5_input(path='../inputs/day5_input.txt', test=False):

    if test:
        path = path.replace('day5', 'day5_test')

    with open(path, 'r') as input:
        cargo = input.read()

    input.close()

    lines = cargo.rstrip().split('\n')

    stacks, moves = split_cargo_manifest(manifest=lines)

    stack_contents = process_cargo_stacks(stacks, test=test)
    moves_processed = process_moves(moves)

    return stack_contents, moves_processed


def move_cargo_step(stacks=None, move=None, reverse=True):

    count = move.get('count')
    src = move.get('source')
    dest = move.get('destination')

    src_stack = stacks.get(src)
    dest_stack = stacks.get(dest)

    count = -1*count
    src_remainder = src_stack[0:count]

    if reverse:
        src_move = src_stack[count:][::-1]
    else:
        src_move = src_stack[count:]

    dest_stack = dest_stack + src_move

    stacks[src] = src_remainder
    stacks[dest] = dest_stack

    return stacks


def follow_cargo_steps(stacks=None, moves=None, reverse=True):

    for move in moves:
        stacks = move_cargo_step(stacks=stacks, move=move, reverse=reverse)

    return stacks


def get_cargo_top(stacks=None, test=False):

    if test:
        max = 3
    else:
        max = 10
    output_str = []
    for i in range(1,max):
        output_str.append(stacks.get(i)[-1])

    return ''.join(output_str)

### Day 6

def get_day6_input(path='../inputs/day6_input.txt'):

    with open(path, 'r') as input:
        stream = input.read()

    input.close()

    return stream.rstrip()


def rolling_window(stream=None, windowsize=4):

    # Pretend it's a stream and we don't know the total number

    match = False
    i = 0

    while match == False:
        size = len(set([x for x in stream[i:windowsize+i]]))
        if size == windowsize:
            match = True
        else:
            i += 1

    return windowsize+i


### Day 7

def get_day7_input(path='../inputs/day7_input.txt'):

    with open(path, 'r') as input:
        directory_struct = input.read()

    input.close()

    return directory_struct.split('\n')


def get_directory_sizes(struct=None):

    folders_flat = {}

    parent_dir = []
    i = 0

    for line in struct:
        #print(line)
        if line.startswith('$ cd'):
            result = re.match(r"[$] cd (.*)",line)

            try:
                if result.groups()[0] == '..':
                    parent_dir.pop()
                    # code to go up one directory to parent dir
                else:
                    current_dir = result.groups()[0]
                    parent_dir.append(current_dir)

                    key = ':'.join(parent_dir)
                    if folders_flat.get(key, None) != None:
                        print('Error - directory already exists', key)
                        break
                    else:
                        #print('adding key to dir dict:', key)
                        folders_flat[key] = []
                        #print(key, folders_flat.get(key))

            except Exception as e:
                print(e)
                raise(e)

        elif line.startswith('$ ls'):
            #print('Parsing Contents for ','/'.join(parent_dir))
            pass
        else:
            if line.startswith('dir'):#Dir Handling
                pass
                #_ , dirname = line.split(' ')
                #print ('/'.join(parent_dir),'/',dirname)
            else:
                try:
                    fsize, fname = line.split(' ')
                    #print('/'.join(parent_dir),'/',fname,':', fsize)
                    directory_path = ':'.join(parent_dir).split(':')
                    while len(directory_path) > 0:
                        dir = ':'.join(directory_path)
                        try:
                            folder_contents = folders_flat.get(dir)
                            folder_contents.append(int(fsize))
                            folders_flat[dir] = folder_contents
                        except Exception as e:
                            print(e, dir, folders_flat.get(dir))
                            raise(e)

                        directory_path.pop()

                except Exception as e:
                    print('Error:',line)
                    raise e

    return folders_flat


def filter_folders(folders=None, thresh=100000):
    return [x for x in folders if x[1] <= thresh]


def get_threshold_totals(folders=None):
    return sum([x[1] for x in folders])


def get_actual_free_space(folders=None, tsize=70000000):

    usize = folders.get('/')

    return tsize - sum(usize)

def get_deletion_size_needed(total_needed=30000000, total_free=None):
    return total_needed - total_free


def find_smallest_ideal_folder(folders=None, thresh=30000000):
    candidates = [x for x in folders if x[1] >= thresh]
    candidates_sorted = sorted(candidates, key=lambda x: x[1])

    return candidates_sorted[0]

### Day 8


def get_day8_input(path='../inputs/day8_input.txt', test=False):

    if test:
         treemap = '30373\n25512\n65332\n33549\n35390'.split('\n')

    else:
        with open(path, 'r') as input:
            treemap = input.read().split('\n')

        input.close()


    return np.array([[int(x) for x in row] for row in treemap])


def check_array_max(arr=None):
    max_forward = [(j > max(np.append(arr[:i], [-1]))) for i,j in enumerate(arr)]
    max_backward = [(j > max(np.append(arr[i+1:], [-1]))) for i,j in enumerate(arr)]

    return [any([x,y]) for (x,y) in zip(max_forward, max_backward)]


def treemap_check(map=None):

    rows = np.apply_along_axis(check_array_max, axis=0, arr=map)
    cols = np.apply_along_axis(check_array_max, axis=1, arr=map)

    return np.sum(np.clip(np.add.reduce([rows,cols]), a_min=0, a_max=1), axis=None)


def get_visible_score_component(arr=None):

    visible_map = []

    for i,j in enumerate(arr):

        visible_forward = 0
        visible_backward = 0

        #for value j at index i, look left 1 by 1
        for ind in reversed(range(0,max(0,max(0,i)))):
            if arr[ind] < j:
                visible_forward +=1
            elif arr[ind] >= j:
                visible_forward +=1
                break
            else:
                print('weird error')


        for ind in range(i+1,len(arr)):
            if arr[ind] < j:
                visible_backward +=1
            elif arr[ind] >= j:
                visible_backward +=1
                break
            else:
                print('weird error')

        visible_map.append(visible_forward*visible_backward)

    return visible_map


def scenic_score(map=None):
    rows = np.apply_along_axis(get_visible_score_component, axis=0, arr=map)
    cols = np.apply_along_axis(get_visible_score_component, axis=1, arr=map)

    return np.multiply(rows,cols)

def get_highest_scenic_score(scores=None):

    return np.max(scores)


### Day 9 Funcs

def get_day9_input(path='../inputs/day9_input.txt', test=False):

    if test:
        #rope_moves = 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2'
        rope_moves = 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20'
    else:
        with open(path, 'r') as input:
            rope_moves = input.read()

        input.close()

    rope_moves = [(x.split(' ')[0], int(x.split(' ')[1])) for x in rope_moves.split('\n')]

    return rope_moves


class Rope():

    head_positions = None
    tail_positions = None

    knots = {}

    move_map = {
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
    'L': np.array([-1,0]),
    'R': np.array([1,0])
    }

    moveset = None
    leader_coords = None
    head_s = None
    tail_s = None

    def __init__(self):
        self.head_positions = []
        self.tail_positions = []
        self.moveset = None
        self.leader_coords = None
        self.head_s = None
        self.tail_s = None
        self.set_start_positions()


    def set_start_positions(self):
        self.head_positions.append(np.array([0,0]))
        self.tail_positions.append(np.array([0,0]))
        self.head_s = np.array([0,0])
        self.tail_s = np.array([0,0])

    def check_adjacent(self, coord1=None, coord2=None):
        cdist = np.abs(coord1 - coord2)
        return max(cdist) <= 1

    def count_tail_positions(self):
        return len(set([tuple(x) for x in self.tail_positions]))

    def process_moveset(self):

        if self.moveset is None:
            print('Rope has no moves to process')
        else:

            for move in self.moveset:
                direction, steps = move

                vector = self.move_map.get(direction, None)

                for step in range(0,steps):
                    #print(self.head_s, self.tail_s)
                    head_pos = self.head_s + vector
                    self.head_positions.append(head_pos)

                    # Check if tail is within 1 and if not move to head_prevpos
                    tail_adjacent = self.check_adjacent(coord1=head_pos, coord2=self.tail_s)
                    #print(head_pos, self.tail_s, 'check distance', tail_adjacent)

                    if tail_adjacent:
                        #print('tail can stay placed')
                        tail_pos = self.tail_s
                    else:
                        #print('tail needs to move')
                        tail_pos = self.head_s
                        self.tail_positions.append(tail_pos)

                    # Set New Start Positions for Next Move
                    self.head_s = head_pos
                    self.tail_s = tail_pos

    def print_moves(self):
        if self.leader_coords is None:
            print('Rope has no moves to process')
        else:
            moves = self.leader_coords
            print(len(moves))


    def process_moves_by_coordinate(self):

        if self.leader_coords is None:
            print('Rope has no moves to process')
        else:
            ldr_crds = self.leader_coords
            for coord in ldr_crds:
                #print('head: ',self.head_s,'->',coord, 'tail: ', self.tail_s)
                head_pos = coord

                self.head_positions.append(head_pos)

                tail_adjacent = self.check_adjacent(coord1=head_pos, coord2=self.tail_s)

                if tail_adjacent:
                    #print('tail can stay where it is')
                    tail_pos = self.tail_s
                else:
                    # ID Move Type:
                    shift_coords = coord - self.head_s
                    if np.abs(shift_coords[0]) > 0 and np.abs(shift_coords[1]) > 0:
                        diagonal = True
                    else:
                        diagonal = False

                    if diagonal:
                        #print('Diagonal Move Detected')
                        if np.array_equal(self.head_s,np.array([0,0])):
                            #print('Head Started on Origin - No Movement Required')
                            tail_pos = self.tail_s
                        elif (head_pos[0] == self.tail_s[0]) or (head_pos[1] == self.tail_s[1]):
                            if head_pos[0] == self.tail_s[0]:
                                new_shift = np.array([0, shift_coords[1]])
                                tail_pos = self.tail_s + new_shift
                                self.tail_positions.append(tail_pos)
                            else:
                                new_shift = np.array([shift_coords[0], 0])
                                tail_pos = self.tail_s + new_shift
                                self.tail_positions.append(tail_pos)

                        else:
                            #print('DIAG - Moving Knot by ', move_type)
                            tail_pos = self.tail_s + shift_coords
                            self.tail_positions.append(tail_pos)
                    else:
                        #print('Moving Knot to Previous Head Position', self.head_s)
                        tail_pos = self.head_s
                        self.tail_positions.append(tail_pos)

                # Set New Start Positions for Next Move
                self.head_s = head_pos
                self.tail_s = tail_pos
                #print('tail now at :', self.tail_s)


def run_knot_simulation(n_knots=10):
    print('initial simulation running')
    #initial rope segment
    rope1 = Rope()
    rope1.set_start_positions()
    rope1.moveset = rope_moves
    rope1.process_moveset()
    rope_tail_coords = rope1.tail_positions
    print(len(rope_tail_coords), 'coordinates to process in next step')
    #print([tuple(x) for x in rope_tail_coords])

    i = 1
    while i < n_knots+1:
        print('knot', i+1, 'simulation')
        rope = Rope()
        rope.set_start_positions()
        rope.leader_coords = rope_tail_coords
        #print('processing moves')
        rope.process_moves_by_coordinate()
        #print('getting coordinates')
        rope_tail_coords = rope.tail_positions
        #print('knot',i,'simulation finished')
        print('total spaces visited for knot',i+1,rope.count_tail_positions())
        #print([rope_tail_coords])
        i+=1


    return rope.count_tail_positions()