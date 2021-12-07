from os.path import dirname

data_dir = dirname(__file__) + '/data'

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

def load_comma_int(fname):
    s = load_str(fname)
    return [int(x) for x in s.split(',')]

def load_csv_array(fname):
    s = load_list_str(fname)
    return [x.split(',') for x in s]

def load_nn_lists_str(fname):
    s = load_str(fname)
    return [x.split() for x in s.split('\n\n')]

advent_data_parser = {
    1: load_list_int,
    2: load_comma_int,
    3: load_csv_array,
    4: load_str,
    5: load_comma_int,
    6: load_nn_lists_str,
    7: load_list_str,
    8: load_list_str,
}