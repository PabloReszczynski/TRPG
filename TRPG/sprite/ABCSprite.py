from abc import ABCMeta

class ABCSprite(metaclass=ABCMeta):
    """
    Abstract class for the sprite system
    """

    def __init__(self, data):
        self.data = data

    def render(self):
        return self.data
