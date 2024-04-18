import sys

import pygame
import pygame.event

import logger
from states.state import State


class EventHandler:
    """EventHandler

    The 'EventHandler' manages the event handlers of the current state.

    """

    @logger.log_trace(logger.Levels.INFO)
    def __init__(self, currentState: State) -> None:
        """__init__

        Initialises the event handler.

        Args:
            currentState (State): Initial game state whose event handlers need to be managed.
        """
        #  Store current game state.

        self._currentState: State = currentState

    @logger.log_trace(logger.Levels.DEBUG)
    def handleEvents(self) -> None:
        """handlerEvents

        Calls each of the event handlers for the current state.
        """
        #  Call event handlers for each event.

        for _event in pygame.event.get():
            self.checkQuitEvent(_event)
            self.checkKeyEvent(_event)
            self.checkMouseEvent(_event)
            self.checkJoystickEvent(_event)

    @staticmethod
    @logger.log_trace(logger.Levels.DEBUG)
    def checkQuitEvent(event: pygame.event.Event) -> None:
        """checkQuitEvent

        Checks if the event passed to it is a quit event and if so quits the game.

        Args:
            event (Event): event to check.
        """
        #  Check event and quit if neeed

        if event.type == pygame.QUIT:
            quit()
            sys.exit()

    @logger.log_trace(logger.Levels.DEBUG)
    def update(self, newState: State) -> None:
        """update

        Sets the new game state.

        Args:
            newState (State): new game state.
        """
        #  Set new game state.

        self._currentState = newState

    @logger.log_trace(logger.Levels.DEBUG)
    def checkKeyEvent(self, event: pygame.event.Event) -> None:
        """checkKeyEvent

        Calls the key event handler for the current game state.

        Args:
            event (Event): event to handle.
        """
        self._currentState.handleKeyEvent(event)

    @logger.log_trace(logger.Levels.DEBUG)
    def checkMouseEvent(self, event: pygame.event.Event) -> None:
        """checkMouseEvent

        Calls the mouse event handler for the current game state.

        Args:
            event (Event): event to handle.
        """
        self._currentState.handleMouseEvent(event)

    @logger.log_trace(logger.Levels.DEBUG)
    def checkJoystickEvent(self, event: pygame.event.Event) -> None:
        """checkJoystickEvent

        Calls the joystick event handler for the current game state.

        Args:
            event (Event): event to handle.
        """
        self._currentState.handleJoystickEvent(event)
