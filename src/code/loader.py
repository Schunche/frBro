if __name__ == "__main__":
    print("Try running \'main.py\' instead")
    exit(0)

import os
import json
import pygame

from src.code.const import \
    Coordinate,\
    Size      ,\
    JsonReturn
from src.code.logger import \
    log_error,\
    log_fatal_error

def load_json(
    path: str
) -> JsonReturn:
    """
    Load a JSON file from the given path.
        WITHOUT \'src/\'
        WITHOUT \'.json\'

    Args:
        path (list[str]): The path to the JSON file.
            WITHOUT '\src\'

    Returns:
        dict: The loaded JSON data.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        Exception: For any other unexpected exceptions.
    """
    try:
        whole_path: str = f"src/{path}.json"
        with open(whole_path, 'r', encoding='utf-8') as file:
            data: JsonReturn = json.load(file)
        del whole_path
        return data
    
    except FileNotFoundError as e:
        log_error(f"The file at path \'{whole_path}\' was not found: {e}")
        del whole_path
        return None
    
    except json.JSONDecodeError:
        log_error(f"The file at path \'{whole_path}\' is not valid JSON: {e}")
        del whole_path
        return None
    
    except Exception as e:
        log_error(f"(unexpected) during loading \'{whole_path}\': {e}")
        del whole_path
        return None

try:
    STGS: dict = load_json(
        "data/settings"
    )
except Exception as e:
    log_fatal_error("Without loading settings, this program can\'t be started")
    exit(1)

WINDOW_SIZE: Size = [
    STGS["window"]["width"],
    STGS["window"]["height"]
]
FPS: int = STGS["window"]["FPS"]
THEME: str = STGS["theme"]

try:
    FIX_STGS: dict = load_json("data/fix_values")
except Exception as e:
    exit(1)

TILE_SIZE: int = FIX_STGS["global"]["tile_size"]

TITLE: str = FIX_STGS["window"]["title"]
RESOLUTIONS: list[Size] = list(FIX_STGS["window"]["allowed_display_resolutions"].values())
FPS_LIST: list[int] = FIX_STGS["window"]["allowed_display_fps"]
CURSOR_LIST: list[None | str] = FIX_STGS["window"]["allowed_cursors"]

COLOR: dict[str, pygame.color.Color] = FIX_STGS["color"]
TRANSPARENT_COLOR: pygame.color.Color = COLOR["transparent_color"]

THEME_STYLE: dict[str, dict[str, str]] = FIX_STGS["theme_style"]

GUI_STGS: dict[str, dict[str]] = FIX_STGS["gui"]

FONT32: pygame.font.Font = pygame.font.Font(None, 32)

def load_image(
    path: str,
    extension: str = "png"
) -> pygame.Surface | None:
    """
    path: without \'src/img/\' and \'.extension\'
    """
    try:
        image: pygame.Surface = pygame.image.load(
            f"src/img/{path}.{extension}"
        )
        image.set_colorkey(
            TRANSPARENT_COLOR
        )
        return image

    except Exception as e:
        log_error(
            f"Couldn't load image: {e}"
        )
        return None
    
def load_text(
    path: str,
    *,
    extension: str = "txt"
) -> list[str] | None:
    """
    Load a txt file from the given path.
        WITHOUT \'src/\'
        WITHOUT \'.txt\'

    Args:
        path (list[str]): The path to the txt file.
            WITHOUT '\src\'

    Returns:
        dict: The loaded txt data.
    """
    try:
        whole_path: str = f"src/{path}.{extension}"
        with open(whole_path, 'r', encoding='utf-8') as file:
            data: list[str] = [line.strip("\n") for line in file]
        del whole_path
        return data
    
    except Exception as e:
        log_error(f"(unexpected) during loading \'{whole_path}\': {e}")
        del whole_path
        return None

CURSOR_SIZE: Size = (24, 24)
SYS_CURSOR: pygame.cursors.Cursor = pygame.mouse.get_cursor()
CURSOR_OFFSET: dict[str, dict[str, Coordinate]] = load_json("data/cursor/offsets")

CURSORS: dict[str, dict[str, pygame.cursors.Cursor]] = {
    cursor_style: {
        cursor_mode.removesuffix(".txt"): pygame.cursors.compile(
            load_text(
                f"data/cursor/{cursor_style}/" + cursor_mode.removesuffix(".txt")
            )
        ) for cursor_mode in os.listdir(
            f"src/data/cursor/{cursor_style}"
        )
    } for cursor_style in os.listdir(
        f"src/data/cursor"
    ) if cursor_style in CURSOR_LIST and cursor_style != "offsets.json"
}
