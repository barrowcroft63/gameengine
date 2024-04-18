import pygame
import pygame.event

import logger
from states.state import State


class State1(State):

    @property
    @logger.log_trace(logger.Levels.DEBUG)
    def nextState(self) -> str:
        """nextState

        Gets the next game state.

        Returns:
            str: the next game state.
        """
        return self._nextState

    @logger.log_trace(logger.Levels.INFO)
    def __init__(self) -> None:
        """__init__

        Initialises the game state.

        """
        self._nextState: str = ""
        self._done: bool = False

    @logger.log_trace(logger.Levels.DEBUG)
    def handleKeyEvent(self, event: pygame.event.Event) -> None:
        """handleKeyEvent

        Handles keyboard events.
        Coordinates the handling of events by other classes.

        Args:
            event (Event): event to handle.
        """
        ...

    @logger.log_trace(logger.Levels.DEBUG)
    def handleMouseEvent(self, event: pygame.event.Event) -> None:
        """handleMouseEvent

        Handles mouse events.
        Coordinates the handling of events by other classes.

        Args:
            event (Event): event to handle.
        """
        ...

    @logger.log_trace(logger.Levels.DEBUG)
    def handleJoystickEvent(self, event: pygame.event.Event) -> None:
        """handleJoystickEvent

        Handles joystick events.
        Coordinates the handling of events by other classes.

        Args:
            event (Event): event to handle.
        """
        ...

    @logger.log_trace(logger.Levels.DEBUG)
    def update(self, dt: float) -> None:
        """udate

        Updates the class.
        Coordinates the updating of all other classes.

        Args:
            dt (float): _description_
        """
        ...

    @logger.log_trace(logger.Levels.DEBUG)
    def render(self, display: pygame.Surface, actualFPS: float) -> None:
        """render

        Renders the class.
        Coordinates the rendering of all other classes.

        Args:
            dt (float): _description_
        """
        ...

    @logger.log_trace(logger.Levels.DEBUG)
    def checkDone(self) -> bool:
        """checkDone

        Checks if the current state is completed.

        Returns:
            bool: true if completed.
        """
        ...

        return self._done
