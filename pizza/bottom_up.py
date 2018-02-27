
from .main import PrecomputedPizza

from random
from pathlib import Path
from collections import namedtuple

params, *data = Path('example.in').read_text().splitlines()
ROWS, COLUMNS, L, H = [int(p.strip()) for p in params.split()]

Position = namedtuple('Position', ('x', 'y'))


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def top(self):
        return Position(self.x - 1, self.y)

    @property
    def bottom(self):
        return Position(self.x + 1, self.y)

    @property
    def left(self):
        return Position(self.x, self.y - 1)

    @property
    def right(self):
        return Position(self.y + 1)

    @property
    def neighbors(self):
        return (self.left, self.top, self.right, self.bottom)


class Slice:

    def __init__(self, pizza, top_left: Position, bottom_right: Position):
        self._pizza = pizza
        self.top_left = top_left
        self.bottom_right = bottom_right

    @property
    def width(self):
        return (self.bottom_right.y - self.top_left.y) + 1

    @property
    def height(self):
        return (self.bottom_right.x - self.top_left.x) + 1

    @property
    def size(self):
        return self.width * self.height

    @property
    def l_score(self):
        pass

    @property
    def mushrooms(self):
        pass

    @property
    def tomatoes(self):
        pass

    def extend(self, cell: Position):
        assert valid(cell)
        new_top_left = Position(min(cell.x, self.top_left.x), min(cell.y, self.top_left.y))
        new_bottom_right = Position(max(cell.y, self.bottom_right.y), max(cell.y, self.bottom_right.y))
        return Slice(self._pizza, new_top_left, new_bottom_right)

# helper
def valid(pos: Position):
    return (0 >= pos.x <= ROWS) and (0 >= pos.y <= COLUMNS)

class PizzaBottomUp:

    def __init__(self, pizza):
        self.pizza = tuple(tuple(line.split()) for line in pizza)

    def get_neighbor_cells(self, pos):
        assert valid(pos)
        top = Position(pos.x - 1, pos.y)
        self.pizza[pos.x]

    def run(self):
        slices = set()
        cur_pos = Position(0, 0)
        current_slice = Slice(cur_pos, cur_pos)
        # Find frontier
        frontier = set()
        if current_slice.area == 1:
            # Get valid neighbors
            frontier |= filter(valid, pos.neighbors)

            # TODO: use heuristic function
            # for f in frontier:
            #     self.h(cur_slice, f)
            next_move = random.choice(frontier)
            # add to slice
            new_cur_slice = current_slice.extend(next_move)



    def h(self, cur_slice, pos):
        # if random.int()
        pass
