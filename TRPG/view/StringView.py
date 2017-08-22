from .ABCView import ABCView
from TRPG.state import GameState

class StringView:
    """
    View class that renders to a String object. For testing purposes.
    """
    def __init__(self, width, height):
        super()
        self.show_state = [('.' * width) for _ in range(height)]

    def show(self, state):
        if not isinstance(state, GameState):
            raise ValueError('State should be a GameState', state)
        for entt in state.entities:
            x = entt.position.x
            y = entt.position.y
            self.show_state[y][x] = entt.render()

    def clear(self):
        self.show_state = ''

ABCView.register(StringView)
