import configparser
import os
from typing import Any

import pygame
import pygame.time

import constants as c
import controller
import logger
from states.state import State
from states.state1 import State1


@logger.log_trace(logger.Levels.INFO)
def getConfig(name: str) -> configparser.ConfigParser:
    """getConfig

    Args:
        name (str): filename to read from.

    Initialises the config parser and reads the config from the given file.
    If the config file does not exist it will be created and default logging level (INFO) set.

    Returns:
        ConfigParser: the config parser.
    """
    _filename = f"{name}.ini"

    _configParser: configparser.ConfigParser = configparser.ConfigParser()

    if os.path.exists(_filename):
        _configParser.read(_filename)
    else:
        _configParser["logging"] = {"logging_level": "INFO"}
        with open(_filename, "w") as configfile:
            _configParser.write(configfile)

    return _configParser


@logger.log_trace(logger.Levels.INFO)
def getDisplay(gameTitle: str) -> pygame.Surface:
    """getDisplay

    Initialises the pygame display.

    Args:
        gameTitle (str): title for screen.

    Returns:
        Surface: main game surface.
    """
    pygame.init()
    pygame.mixer.init()

    _flags = pygame.DOUBLEBUF | pygame.NOFRAME
    # _display: Surface = display.set_mode(SCREEN_SIZE, _flags)
    _display: pygame.Surface = pygame.display.set_mode(c.SCREEN_SIZE, _flags)
    pygame.display.set_caption(gameTitle)

    return _display


@logger.log_trace(logger.Levels.INFO)
def getClock() -> pygame.time.Clock:
    """getClock

    Initialises the clock.

    Returns:
        Clock: the clock.
    """
    _clock: pygame.time.Clock = pygame.time.Clock()

    return _clock


@logger.log_trace(logger.Levels.INFO)
def getGameStates() -> dict[str, State]:
    """getGameStates

    Initialises the dictionary containing the game states.

    Returns:
        dict[str, State]: dictionary of game states.
    """
    _gamestates: dict[str, Any] = {
        c.GAME_STATE: State1,
    }
    return _gamestates


@logger.log_trace(logger.Levels.INFO)
def getController(
    display: pygame.Surface,
    clock: pygame.time.Clock,
    gamestates: dict[str, State],
    startingState: str,
) -> controller.Controller:
    """getController

    Gets the game controller.

    """
    _controller: controller.Controller = controller.Controller(
        display, clock, gamestates, startingState
    )

    return _controller
