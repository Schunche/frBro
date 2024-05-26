if __name__ == "__main__":
    print("Try running \'main.py\' instead")
    exit(0)

import json

from src.code.logger import \
    log_error

def load_json(
    path: str
) -> list | dict | str | int | float | bool | None:
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
            data = json.load(file)
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

STGS: dict = load_json("data/settings")
WINDOW_SIZE: list[int] = [
    STGS["window"]["width"],
    STGS["window"]["height"]
]
FPS: int = STGS["window"]["FPS"]
THEME: str = STGS["theme"]

FIX_STGS: dict = load_json("data/fix_values")
TITLE: str = FIX_STGS["window"]["title"]
COLOR: dict[str, list[int]] = FIX_STGS["color"]
TRANSPARENT_COLOR: list[int] = COLOR["transparent_color"]

import pygame

def load_image(
    path: str,
    extension: str = "png"
):
    
    try:
        image: pygame.Surface = pygame.image.load(
            f"src/img/{path}.{extension}"
        )
    except Exception as e:
        log_error(
            f"Unaccounted: {e}"
        )
