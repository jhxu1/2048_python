import random
from common.status import StatusCode
from common.player import Player
from common.tools import _logger

class TwoZeroFourEightGame:
    def __init__(self, config) -> None:
        self.config = config
        self.name = config['name']
        self.status = StatusCode.UNACTIVATED
        self.screen = None
        self._end_num = config.get("end_num", 2048)
        self.players = {}

    def init_screen(self):
        try:
            screen = TwoZeroFourEightScreen(self.config)
            screen.init()
        except Exception as e:
            _logger.error(f"Screen init failed with exception {e}")
            raise e
        return screen

    def add_player(self, player):
        self.players[player.id] = TwoZeroFourEightPlayer.gen_by_player(player)
        player.cur_game = self

    def remove_player(self, player):
        assert player._cur_game == self
        assert player.id in self.players.keys()
        player.cur_game = None
        del self.players[player.id]

    def start(self):
        if self.status == StatusCode.RUNNING:
            _logger.warning("Game is already running")
        self.screen = self.init_screen()
        self.status = StatusCode.RUNNING
        _logger.info(f"Start game {self.name}")

    def restart(self):
        self.status == StatusCode.UNACTIVATED
        self.start()

    def check(self):
        assert self.status == StatusCode.RUNNING, f"Error status {self.status}"

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
        self.config = config

    def init(self):
        try:
            self._random_init(self.config["init_num"])
        except Exception as e:
            raise e

    def show(self):
        """打印到屏幕上"""
        for row_data in self._data:
            row_data = ["x" for d in row_data if d is None]
            row_data = [str(d) for d in row_data]
            _logger.info(" ".join(row_data))

    def _gen_random_num_2(self):
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

    def _random_init(self, init_num):
        for _ in range(init_num):
            try:
                self._random_gen_block()
            except Exception as e:
                raise e

    def _random_gen_block(self):
        if self._blank_num == 0:
            raise Exception("Screen if full!")

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

