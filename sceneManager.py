import pygame

class SceneManager():

    def __init__(self):
        self._option = []
        self._callbacks = []
        self._current_option_index = 0
        self._isSwitch = False

    def append_option(self, option, callback):
        self._option.append(option)
        self._callbacks.append(callback)

    def set_current_option_index(self, option_index):
        self._current_option_index = option_index
        self._isSwitch = True

    def get_isSwitch(self):
        return self._isSwitch

    def select(self):
        self._callbacks[self._current_option_index]()
        self._isSwitch = False

    def draw(self):
        self._callbacks[self._current_option_index]()


