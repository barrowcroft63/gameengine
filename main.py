import configparser

import pygame
import pygame.time

import constants as c
import controller
import init
import logger
from states.state import State


@logger.log_trace(logger.Levels.INFO)
def main() -> None:
    """main

    The main program entry.
    Sets up all the elements of the game engine.

    """
    #  Read the configuration file (create it if it doesn't exist) and set logging level.

    _configParser: configparser.ConfigParser = init.getConfig(c.GAME_NAME)
    _loggingLevel = _configParser.get("logging", "logging_level")
    logger.log_level(_loggingLevel)

    #  Get the pygame display surface.

    _display: pygame.Surface = init.getDisplay(c.GAME_TITLE)

    #  Get the pygame clock.

    _clock: pygame.time.Clock = init.getClock()

    #  Load the game states.

    _gameStates: dict[str, State] = init.getGameStates()

    _controller: controller.Controller = init.getController(
        _display, _clock, _gameStates, c.INITIAL_STATE
    )
    _controller.run_game()


if __name__ == "__main__":
    main()
