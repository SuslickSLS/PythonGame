import pygame

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0



    def append_option(self, option, callback ):
        self._option_surfaces.append(pygame.font.Font('.venv/Font/Silkscreen [RUS by Mr.Enot].ttf', 50).render(option, True, ('black')))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))
        pass

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, ('blue'), option_rect)
            surf.blit(option, option_rect)