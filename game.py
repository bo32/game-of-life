from grid import Grid

class Game:
    def __init__(self):
        self.grid = Grid(30, 30)

    def live(self, frequency: int = 1000):
        self.grid.live(frequency)

if __name__ == "__main__":
    game = Game()

    # Glider
    game.grid.add_alive_cell_at(2,10)
    game.grid.add_alive_cell_at(3,10)
    game.grid.add_alive_cell_at(4,10)
    game.grid.add_alive_cell_at(4,9)
    game.grid.add_alive_cell_at(3,8)

    game.grid.add_alive_cell_at(8,10)
    game.grid.add_alive_cell_at(9,9)
    game.grid.add_alive_cell_at(10,9)
    game.grid.add_alive_cell_at(9,10)
    game.grid.add_alive_cell_at(10,10)
    game.grid.add_alive_cell_at(11,13)
    game.grid.add_alive_cell_at(11,12)
    game.grid.add_alive_cell_at(10,11)
    game.grid.add_alive_cell_at(11,20)
    game.grid.add_alive_cell_at(11,21)
    game.grid.add_alive_cell_at(11,22)
    game.live(500)