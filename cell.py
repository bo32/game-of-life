class Cell:

    def __init__(self, alive=False):
        self.alive = alive
        self.will_survive = False

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def live(self):
        if self.is_alive():
            if self.are_two_or_three_alive_neighbours():
                self.will_survive = True
            else:
                self.will_survive = False
        else:
            if self.are_three_alive_neighbours():
                self.will_survive = True
            else:
                self.will_survive = False

    def set_alive(self, alive: bool = True) -> bool:
        self.alive = alive
        self.will_survive = alive


    def is_alive(self) -> bool:
        return self.alive

    def are_two_or_three_alive_neighbours(self)-> bool:
        return self.are_three_alive_neighbours() or self.are_two_alive_neighbours()

    def are_three_alive_neighbours(self) -> bool:
        return self.get_alive_neigbours_count() == 3
    
    def are_two_alive_neighbours(self) -> bool:
        return self.get_alive_neigbours_count() == 2

    def get_alive_neigbours_count(self) -> int:
        return len(list(neighbour for neighbour in self.neighbours if neighbour.is_alive()))
        