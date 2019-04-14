from enum import Enum


# This constraint means that from direction 'direction' there should be visible N buildings
# Directions:
# G - up
# D - down
# L - left
# P - right


class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3


def create_N_N_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        matrix.append(row)
    return matrix



class ConstraintSkyscrapper:

    def parse_direction(self, direction):
        if direction == 'G':
            self.direction = Direction.up
        elif direction == 'D':
            self.direction = Direction.down
        elif direction == 'L':
            self.direction = Direction.left
        elif direction == 'P':
            self.direction = Direction.right
        else:
            raise Exception('Impossible direction value')

    def __init__(self, direction, index, N):
        self.parse_direction(direction)
        self.index = index
        self.N = N

    def __eq__(self, other):
        return self.direction == other.direction and self.N == other.N

    def __repr__(self):
        return 'Skyscrapper constraints, direction:  ' + str(self.direction) + ', index:' + str(self.index)  +', no of visible buildings: ' + str(self.N)


class BoardSkyscrapper:

    def __init__(self, N, constraints):
        self.N = N
        self.matrix = create_N_N_matrix(N)
        self.constraints = constraints

    def move_sanity_check(self, x, y, value):
        pass
