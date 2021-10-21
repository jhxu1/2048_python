import random
from common.status import StatusCode
from common.player import Player

class TwoZeroFourEightGame:
    def __init__(self, config) -> None:
        self.config = config
        self.status = StatusCode.RUNNING
        self.screen = self.init_screen()
        self._end_num = config["end_num"]
        self.players = {}

    def init_screen(self):
        screen = TwoZeroFourEightScreen(self.config)
        return screen

    def add_player(self, player):
        self.players[player.id] = player
        player.cur_game = self

    def remove_player(self, player):
        assert player._cur_game == self
        assert player.id in self.players.keys()
        player.cur_game = None
        del self.players[player.id]

    def check(self):
        if self.status == StatusCode.RUNNING:
            pass
        elif self.status == StatusCode.SUCCESS:
            print("Success!")
            exit()
        else:
            raise Exception("Get exception: {}".format(self.status))

    def _move_up(self):
        for col in range(self.screen._width):
            num_row = 0
            for row in range(num_row+1, self._height):
                if self.screen[row][col] == 'X':
                    continue
                else:
                    if self.screen[num_row][col] == 'X':
                        self.screen[num_row][col], self.screen[row][col] = self.screen[row][col], 'X'
                    else:
                        # same
                        if self.screen[num_row][col] == self.screen[row][col]:
                            self.screen[num_row][col] *= 2
                            self.screen[row][col] = 'X'
                        else:
                            pass
                        num_row += 1
                        
    def _move_down(self):
        self.screen = self.screen[::-1]
        self._move_up()
        self.screen = self.screen[::-1]

    def _move_left(self):
        for row in range(self._height):
            num_col = 0
            for col in range(num_col+1, self.screen._width):
                if self.screen[row][col] == 'X':
                    continue
                else:
                    if self.screen[row][num_col] == 'X':
                        self.screen[row][num_col], self.screen[row][col] = self.screen[row][col], 'X'
                    else:
                        # same
                        if self.screen[row][num_col] == self.screen[row][col]:
                            self.screen[row][num_col] *= 2
                            self.screen[row][col] = 'X'
                        else:
                            pass
                        num_col += 1

    def _move_right(self):
        self.screen = [d[::-1] for d in self.screen]
        self._move_left()
        self.screen = [d[::-1] for d in self.screen]

    def _check_success(self,):
        for row_data in self.screen:
            for data in row_data:
                if data == self._end_num:
                    return True
        return False 

    def _random_init(self, init_num):
        for _ in range(init_num):
            flag = self._random_gen_block()
            if not flag:
                return StatusCode.INIT_ERROR

    def _random_gen_block(self):
        if self.screen.blank_num == 0:
            self.status = StatusCode.FAILED
            return False

class TwoZeroFourEightPlayer(Player):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def _press_button_a(self):
        return self._cur_game.move_left()

    def _press_button_s(self):
        return self._cur_game.move_down()

    def _press_button_w(self):
        return self._cur_game.move_up()

    def _press_button_d(self):
        return self._cur_game.move_right()

class TwoZeroFourEightScreen:
    """Screen
    """
    def __init__(self, config) -> None:
        self._height = config["height"]
        self._width = config["width"]
        self._data = [[None for _ in range(self._width)] for _ in range(self._height)]
        self._blank_num = self._height * self._width
        self.status = StatusCode.RUNNING
        self._random_init(config["init_num"])

    def show(self):
        """打印到屏幕上"""
        for row_data in self._data:
            row_data = ["x" for d in row_data if d is None]
            row_data = [str(d) for d in row_data]
            print(" ".join(row_data))

    def _gen_random_2(self):
        assert self.blank_num > 0
        all_num = self._width * self._height
        while True:
            rand_idx = random.randint(0, all_num-1)
            row, col = divmod(rand_idx, self._width)
            if self._data[row][col] == None:
                self._data[row][col] = 2
                self.blank_num -= 1
                break
        return True

    @property
    def blank_num(self):
        return self._blank_num

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def __getitem__(self, idxy):
        idx, idy = idxy
        return self._data[idx][idy]

    @property
    def data(self):
        return self._data

