class GameEntity:
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def match(self, parameters):
        for key, value in parameters.items():
            if not getattr(self, key) == value:
                return False
        return True

    def render(self):
        if getattr(self, 'sprite') is not None:
            return self.sprite.render()
        else:
            raise ValueError('This game entity doesnt have a Sprite!')

    def __repr__(self):
        return 'GameEntity %s' % repr(self.__dict__)
