import time
import os

from cell import Cell

ALIVE_REPRESENTATION = '\u25A0' # filled square

class Grid:
    def __init__(self, width = 50, height = 50):
        self.width = width
        self.height = height

        self.cells = []
        # Init cells
        for i in range(self.height):
            self.cells.append([])
            for j in range(self.width):
                self.cells[i].append(Cell())

        # Assign neighbours
        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.find_neighbours_of_cell_at(i, j)
                self.cells[i][j].set_neighbours(neighbours)

    def find_neighbours_of_cell_at(self, i, j):
        neighbours = []

        if i > 0:
            # N
            neighbours.append(self.cells[i - 1][j])
            if j > 0:
                # NW
                neighbours.append(self.cells[i - 1][j - 1])
            if j < self.width - 1:
                # NE
                neighbours.append(self.cells[i - 1][j + 1])

        if i < self.height - 1:
            # S
            neighbours.append(self.cells[i + 1][j])
            if j > 0:
                # SW
                neighbours.append(self.cells[i + 1][j - 1])
            if j < self.width - 1:
                # SE
                neighbours.append(self.cells[i + 1][j + 1])
        
        if j > 0:
            # W
            neighbours.append(self.cells[i][j - 1])
        if j < self.width - 1:
            # E
            neighbours.append(self.cells[i][j + 1])

        return neighbours

    def add_alive_cell_at(self, i: int, j: int):
        self.cells[i][j].set_alive()

    def live(self, frequency):
        self.draw()
        while True:
            time.sleep(frequency / 1000)

            for i in range(self.width):
                for j in range(self.height):
                    self.cells[i][j].live()    
            self.draw()

            for i in range(self.width):
                for j in range(self.height):
                    self.cells[i][j].alive = self.cells[i][j].will_survive
                    self.cells[i][j].will_survive = False
                    

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        top_line = '+' + '-' * (self.width * 2 - 1) + '+'
        print(top_line)
        for i in range(self.height):
            line = '|'
            for j in range(self.width):
                line = line + (ALIVE_REPRESENTATION if self.cells[i][j].will_survive else ' ') + '|'
            print(line)
        print(top_line)
        print(' ')
        print(' ')
    





    