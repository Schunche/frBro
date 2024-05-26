if __name__ == "__main__":
    print("Try running \'main.py\' instead")
    exit(0)

import os
import json

from dataclasses import \
    dataclass,\
    field
from typing import \
    Self

from src.code.logger import \
    log_fatal_error,\
    log_success
from src.code.const import \
    Coordinate,\
    Tile
from src.code.loader import \
    load_json

@dataclass
class Map:
    tilemap: dict[Coordinate, Tile]

    def __post_init__(
        self: Self
    ) -> None:
        pass

def get_all_map_names() -> list[str]:
    return [
        map_name.removesuffix(
            ".json"
        ) for map_name in os.listdir(
            "src/map"
        )
    ]

def load_map(
    path: str
) -> Map | None:
    rmap: dict[str, dict] = load_json(
        f"map/{path}"
    )
    if rmap is None:
        log_fatal_error(
            f"Couldn\'t load \'{path}\'"
        )
        return None
    
    rtilemap: dict[Coordinate, Tile] = {}
    for str_key, value in rmap["tilemap"].items():
        key_parts = str_key.split(';')
        key = (int(key_parts[0]), int(key_parts[1]))
        rtilemap[key] = value

    return Map(
        rtilemap
    )