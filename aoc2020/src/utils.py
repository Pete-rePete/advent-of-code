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
    print(__file__)
    print(data_dir)
    with open(fname, 'r') as f:
        s = f.read()
    return [int(x) for x in s.split('\n')]

advent_data_parser = {
    1: load_list_int
}