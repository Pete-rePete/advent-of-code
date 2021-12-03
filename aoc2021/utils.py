from os.path import dirname

data_dir = dirname(dirname(__file__)) + '/data'

def data(day_num):
    '''
    All data files stored in data_dir with filename like:
        "day1", "day2", etc
    '''
    load_fn = advent_data_parser[day_num]
    return load_fn(data_dir + "/day" + str(day_num))


def load_list_int(fname):
    return [int(x) for x in load_list_str(fname)]

def load_list_str(fname):
    with open(fname, 'r') as f:
        s = f.read().strip()
    return s.split('\n')

def load_str(fname):
    with open(fname, 'r') as f:
        s = f.read().strip()
    return s

def load_nn_lists_str(fname):
    s = load_str(fname)
    return [x.split() for x in s.split('\n\n')]

advent_data_parser = {
    1: load_list_int
}