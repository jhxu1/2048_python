import random
from status import StatusCode

class Screen:
    def __init__(self, height=5, width=5, init_num=3, end_num=2048) -> None:
        self._height = height
        self._width = width
        self._data = [['X' for _ in range(width)] for _ in range(height)]
        self.blank_num = self._height * self._width
        self.status = StatusCode.RUNNING
        self._end_num = end_num

        self._random_init(init_num)

    def show(self):
        """打印到屏幕上"""
        for row_data in self._data:
            row_data = [str(d) for d in row_data]
            print(" ".join(row_data))

    def move(self, cmd):
        if cmd == 'w':
            self._move_up()
        elif cmd == 's':
            self._move_down()
        elif cmd == 'a':
            self._move_left()
        elif cmd == 'd':
            self._move_right()
        else:
            self.status = StatusCode.COMMAND_ERROR
            return False
        if self._check_success():
            self.status = StatusCode.SUCCESS
            return True

    def check(self):
        if self.status == StatusCode.RUNNING:
            pass
        elif self.status == StatusCode.SUCCESS:
            print("Success!")
            exit()
        else:
            raise Exception("Get exception: {}".format(self.status))

    def _check_success(self,):
        for row_data in self._data:
            for data in row_data:
                if data == self._end_num:
                    return True
        return False

    def _move_up(self):
        for col in range(self._width):
            num_row = 0
            for row in range(self._height):
                if self._data[row][col] == 'X':
                    continue
                else:
                    if self._data[num_row][col] == 'X':
                        self._data[num_row][col], self._data[row][col] = self._data[row][col], 'X'
                    else:
                        # same
                        if self._data[num_row][col] == self._data[row][col]:
                            self._data[num_row][col] *= 2
                            self._data[row][col] = 'X'
                        else:
                            num_row += 1
                            self._data[num_row][col], self._data[row][col] = self._data[row][col], 'X'
                        
    def _move_down(self):
        self._data = self._data[::-1]
        self._move_up()
        self._data = self._data[::-1]

    def _move_left(self):
        for row in range(self._height):
            num_col = 0
            for col in range(self._width):
                if self._data[row][col] == 'X':
                    continue
                else:
                    if self._data[row][num_col] == 'X':
                        self._data[row][num_col], self._data[row][col] = self._data[row][col], 'X'
                    else:
                        # same
                        if self._data[row][num_col] == self._data[row][col]:
                            self._data[row][num_col] *= 2
                            self._data[row][col] = 'X'
                        else:
                            num_col += 1
                            self._data[row][num_col], self._data[row][col] = self._data[row][col], 'X'

    def _move_right(self):
        self._data = [d[::-1] for d in self._data]
        self._move_left()
        self._data = [d[::-1] for d in self._data]

    def _random_init(self, init_num):
        for _ in range(init_num):
            flag = self._random_gen_block()
            if not flag:
                return StatusCode.INIT_ERROR

    def _random_gen_block(self):
        if self.blank_num == 0:                     # 失败
            self.status = StatusCode.FAILED
            return False
        all_num = self._width * self._height
        while True:
            rand_idx = random.randint(0, all_num-1)
            row, col = divmod(rand_idx, self._width)
            if self._data[row][col] == 'X':
                self._data[row][col] = 2
                self.blank_num -= 1
                break
        return True

if __name__ == '__main__':
    test_screen = Screen()
    test_screen.show()