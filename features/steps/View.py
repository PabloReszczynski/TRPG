from TRPG.view import StringView
from TRPG.state import GameState
from behave import *
import sure

@given(u'a game state, a view instance')
def step_impl(context):
    context.view = StringView(14, 1)
    context.state = GameState()
    context.state.registerState('this is a map')

@when(u"the method 'show' is called with the state")
def step_impl(context):
    context.view.show(context.state)

@then(u'the view should output some graphics in a screen.')
def step_impl(context):
    (context.view.show_state).should.be.equal('this is a map')
