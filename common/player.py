import abc

class Player(metaclass=abc.ABCMeta):
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self._cur_game = None

    @property
    def cur_game(self):
        return self._cur_game

    @cur_game.setter
    def cur_game(self, game):
        self._cur_game = game

    def press_button(self, buttom):
        return {
            "w": self._press_button_w,
            "a": self._press_button_a,
            "s": self._press_button_s,
            "d": self._press_button_d
        }[buttom]()

    def _press_button_w(self):
        raise NotImplementedError

    def _press_button_s(self):
        raise NotImplementedError

    def _press_button_a(self):
        raise NotImplementedError

    def _press_button_d(self):
        raise NotImplementedError

    def _press_button_up(self):
        raise NotImplementedError

    def _press_button_down(self):
        raise NotImplementedError

    def _press_button_left(self):
        raise NotImplementedError

    def _press_button_right(self):
        raise NotImplementedError
