Feature: Abstract View Class
  In order to play the game
  As an User
  I want to view the game state and interact with it

  Scenario: Displaying the game state
    Given a game state, a view instance
    When the method 'show' is called with the state
    Then the view should output some graphics in a screen.

