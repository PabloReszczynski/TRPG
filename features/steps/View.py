from TRPG.view import ABCView
from TRPG.state import GameState
from behave import *
import sure

class MockView:

    def __init__(self):
        super()
        self.show_state = ''

    def show(self, state):
        self.show_state = state.state

    def clear(self):
        self.show_state = ''

ABCView.register(MockView)

@given(u'a game state, a view instance')
def step_impl(context):
    context.view = MockView()
    context.state = GameState()
    context.state.registerState('this is a map')

@when(u"the method 'show' is called with the state")
def step_impl(context):
    context.view.show(context.state)

@then(u'the view should output some graphics in a screen.')
def step_impl(context):
    (context.view.show_state).should.be.equal('this is a map')
