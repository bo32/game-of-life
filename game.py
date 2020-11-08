from grid import Grid

from pathlib import Path

class Game:
    def __init__(self, init_filepath_str: str = None):
        if init_filepath_str is not None:
            if not Path(init_filepath_str).exists():
                sys.exit("file %s doesn't exist.".format(init_filepath_str))
            self.init_from_filepath(init_filepath_str)
        else:
            self.grid = Grid(30, 30)

    def live(self, frequency: int = 1000):
        self.grid.live(frequency)

    def init_from_filepath(self, init_filepath_str: str) -> tuple:
        lines = self.get_lines_from(init_filepath_str)
        first_line = lines[0].strip()
        width = (len(first_line) - 1) / 2
        height  = len(lines) - 2
        self.grid = Grid(int(width), height)

        content_lines = lines[1:-1]
        for i, line in enumerate(content_lines):
            for j, character in enumerate(list(character for character in line.strip() if character != '|')):
                if character != ' ':
                    self.grid.add_alive_cell_at(i,j)

    def get_lines_from(self, init_filepath_str: str):
        with open(init_filepath_str) as init_file:
            return init_file.readlines()

if __name__ == "__main__":
    game = Game('inits/init.txt') # <- I found this iniial situation a bit randomly, but is very cool!
    game.live(500)