import pygame


class videoGame:
    def __init__(self, window_width=800, window_height=600, window_title="myGame"):
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._is_game_over = False
        if not pygame.font:
            print("Warning, fonts disabled")
        if not pygame.mixer:
            print("Warning, sound disabled")
        self._screen_graph = None

    def run(self):
        while not self._is_game_over:
            current_scene = self.get_next_scene()
            current_scene.start()
            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate)
                for event in pugame.event.get():
                    scence.process_event(event)
                current_scene.update()
                current_scene.draw(self._screen)
                pygame.display.update()
            current_scene.end()


class myRange:
    def __init__(self, stop):
        self._start = 0
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            yield self._start
            self._start += 1
            if self._start < self._stop:
                raise StopIteration()
