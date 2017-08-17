from TRPG.entities import GameEntity

class GameState:

    def __init__(self):
        self.entities = []

    def registerState(self, state):
        self.state = state

    def addEntity(self, entity):
        if not isinstance(entity, GameEntity):
            raise ValueError('Object %s is not an instance of GameEntity' %
                             entity)
        self.entities.append(entity)

    def find_entity(self, parameters):
        return [entt for entt in self.entities if entt.match(parameters)][0]

