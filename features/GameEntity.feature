Feature: Game Entity
  In order to play the game
  As an User
  I want to interact with multiple individual Entities

  Scenario: Creating an Entity
    Given a game state
    When a Game Entity is created and added to the state
    Then the state should update with the new Entity data

  Scenario: Showing an Entity on a screen
    Given an Entity with a Sprite, a GameState and a View
    When the state is displayed in the view
    Then the view should show the entity Sprite

