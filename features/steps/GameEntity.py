from TRPG.entities import GameEntity
from TRPG.state import GameState
from TRPG.util import Position
from TRPG.view import StringView
from TRPG.sprite import StringSprite
from behave import *
import sure

@given('a game state')
def step_impl(context):
    context.state = GameState()

@when('a Game Entity is created and added to the state')
def step_impl(context):
    entity_data = {
        'id': 1,
        'name': 'an entity',
        'position': Position(0, 0, 0)
    }
    entt = GameEntity(entity_data)
    context.entt = entt
    context.state.addEntity(entt)

@then('the state should update with the new Entity data')
def step_impl(context):
    context.state.find_entity({'id': 1}).should.be.equal(context.entt)


@given('an Entity with a Sprite, a GameState and a View')
def step_impl(context):
    view = StringView(5, 1)
    state = GameState()
    entt_data = {
        'sprite': StringSprite('#'),
        'position': Position(0, 0, 0)
    }
    entt = GameEntity(entt_data)
    state.addEntity(entt)
    context.state = state
    context.view = view

@when('the state is displayed in the view')
def step_impl(context):
    context.view.show(context.state)

@then('the view should show the entity Sprite')
def step_impl(context):
    (context.view.show_state).should.be.equal('#')
