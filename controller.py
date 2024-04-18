from typing import Any

import pygame
import pygame.time

import eventhandler
from states.state import State

FPS = 80

import logger


class Controller:
    """Controller

    The 'Controller' handles the running of the game state loop.
    It is given a starting game state and runs the game loop until the state changes.
    The 'Controller' then runs the new game state until another change happens. etc

    """

    @logger.log_trace(logger.Levels.INFO)
    def __init__(
        self,
        display: pygame.Surface,
        clock: pygame.time.Clock,
        States: dict[str, Any],
        startingState: str,
    ) -> None:
        """__init__

        Initalises the 'Controller'.

        Args:
            display (Surface): Surface onto which the game state will be rendered.
            clock (Clock): Game clock.
            States (Dict[str, Any]): Dictionary of game states.
            startingState (str): Starting game state.
        """
        #  Setup surface and clock.

        self._display: pygame.Surface = display
        self._clock: pygame.time.Clock = clock

        #  Store game states for later reference.

        self._States: dict[str, Any] = States

        #  Start event handler for current state.

        self._currentState: State = self._States[startingState]()
        self._eventHandler: eventhandler.EventHandler = eventhandler.EventHandler(
            self._currentState
        )

    @logger.log_trace(logger.Levels.INFO)
    def run_game(self) -> None:
        """run_game

        THIS IS THE MAIN GAME LOOP.

        """
        #  Loop until the game is cancelled.

        while True:
            #  Check to see if state has changed.

            self.update()

            #  Update clock and actual frames per second.

            dt: float = self._clock.tick(FPS) / 1000
            actualFPS: float = self._clock.get_fps()

            #  Handle events, update state and render.

            self._eventHandler.handleEvents()
            self._currentState.update(dt)
            self._currentState.render(self._display, actualFPS)

            #  Update display.

            pygame.display.flip()  #  type: ignore

    @logger.log_trace(logger.Levels.DEBUG)
    def update(self) -> None:
        """update

        Check to see in the current game state has finished and sets next game state.

        """
        if self._currentState.checkDone():

            #  Clear the display.

            self._display.fill((0, 0, 0, 1))

            #  Get next state.

            self._currentState = self._States[self._currentState.nextState]()

            #  Update the event handler to handle the new state.

            self._eventHandler.update(self._currentState)
