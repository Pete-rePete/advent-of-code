import utils

def parse_instruction(instr):
    direction = instr[0]
    distance = int(instr[1:])
    return direction, distance

def lay_down_wire_length(pos, instr):
    '''
    coordinate system X,Y
    U corresponds with positive Y
    D negative Y
    L negative X
    R positive X

    Arguments:
        pos [tuple]: Position. XY coordinates
        instr [str]: Instruction. e.g. "U12" means "up 12"

    Returns
        wire [list] list of coordinates where wire has been laid down
        pos [tuple] (X,Y) coordinate of new position, at the end of the new wire length
    '''
    drc, dist = parse_instruction(instr)
    L = 1 if drc == 'L' else 0
    R = 1 if drc == 'R' else 0
    U = 1 if drc == 'U' else 0
    D = 1 if drc == 'D' else 0
    wire = []
    for x in range(1,dist+1):
        pos = (pos[0] - L + R, pos[1] + U - D)
        wire.append(pos)
    return wire, pos

def lay_down_full_wire(instrs):
    last_pos = (0,0)
    wire = []
    for instr in instrs:
        new_length, last_pos = lay_down_wire_length(last_pos, instr)
        wire.extend(new_length)
    return wire

def print_map(wire1, wire2):
    t_wire1 = list(map(list, zip(*wire1)))
    t_wire2 = list(map(list, zip(*wire2)))
    xmin = min(min(t_wire1[0]), min(t_wire2[0]))
    ymin = min(min(t_wire1[1]), min(t_wire2[1]))
    xoffset = xmin if xmin < 0 else 0
    yoffset = ymin if ymin < 0 else 0
    xmax = max(max(t_wire1[0]), max(t_wire2[0])) - xoffset + 1
    ymax = max(max(t_wire1[1]), max(t_wire2[1])) - yoffset + 1
    wmap = [['.' for x in range(xmax)] for y in range(ymax)]
    wmap[-yoffset][-xoffset] = 'o'
    for coord in wire1:
        wmap[coord[1]-yoffset][coord[0]-xoffset] = "*"
    for coord in wire2:
        if wmap[coord[1]-yoffset][coord[0]-xoffset] == ".":
            wmap[coord[1]-yoffset][coord[0]-xoffset] = "+"
        else:
            wmap[coord[1]-yoffset][coord[0]-xoffset] = "X"
    print('\n')
    for row in reversed(wmap):
        print(''.join(row))

def find_x_distances(wire, intersections):
    '''
    Take intersection coordinates and map them sequentially to a wire
    inputs with the number of steps it takes to get to an intersection
    inputs:
        wire [list]:
            Sequential coordinates that make up the wire
        intersections [set]:
            A set of intersections
    outputs:
        intersection_dists [dict]:
             keys = intersection points, 
             values = distance to get there
    '''
    intersection_dists = {}
    for coord in intersections:
        if coord in intersections and coord not in intersection_dists:
            intersection_dists[coord] = wire.index(coord) + 1
    return intersection_dists


def part_a(instrs):
    print("part A")
    wire1 = lay_down_full_wire(instrs[0])
    wire2 = lay_down_full_wire(instrs[1])
    intersections = set(wire1).intersection(set(wire2))
    #print_map(wire1,wire2)
    min_dist = float('inf')
    for i in intersections:
        dist = sum([abs(i[0]), abs(i[1])])
        min_dist = dist if dist < min_dist else min_dist
    print(min_dist)

def part_b(instrs):
    print("part B")
    wire1 = lay_down_full_wire(instrs[0])
    wire2 = lay_down_full_wire(instrs[1])
    #print_map(wire1,wire2)
    intersections = set(wire1).intersection(set(wire2))
    w1_dists = find_x_distances(wire1, intersections)
    w2_dists = find_x_distances(wire2, intersections)
    min_dist = float('inf')
    for x in intersections:
        dist = w1_dists[x] + w2_dists[x]
        if dist < min_dist:
            min_dist = dist
    print(min_dist)

def str_input(s):
    return [y.strip().split(',') for y in s.split('\n')]

if __name__=='__main__':
    instructions = utils.data(3)
    #instructions = str_input('''R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83''')
    part_a(instructions)
    part_b(instructions)
    
