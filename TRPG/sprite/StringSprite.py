from .ABCSprite import ABCSprite

class StringSprite:
    """
    Represents a Sprite with a single char
    """
    def __init__(self, data):
        data = str(data)
        self.data = data
        self.size = self.__getSize(data)

    def __getSize(self, data):
        """Calculates the size of the sprite"""
        dataLines = data.split('\n')
        height = len(dataLines)
        width = max(dataLines, key=len)
        return height * width

ABCSprite.register(StringSprite)
