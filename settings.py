from os import path

WIDTH = 1440
HEIGHT = 720

BOARD_SIZE = 6
ENEMIES_COUNT = (BOARD_SIZE**2)//6

FONT = ("Lucida Sans Typewriter", 20)
FONT_UNDER = ("Lucida Sans Typewriter", 20, "underline")

DIFFICULTIES = ["Normal", "Hard", "Lunatic", "Infernal"]
STYLES = ["FE1", "FE2", "FE3", "FE4", "FE5", "FE6", "FE7", "FE8"]

TILESET_PATH = path.dirname(__file__)+r"\images\all_tilesets.png"

SOUND_PATH = path.dirname(__file__) + "\sounds\\"