import os

from src.code.loader import \
    FIX_STGS

class GravityEntity:
    def __init__():
        pass

class TileCollider:
    def __init__():
        pass

class Mob(GravityEntity, TileCollider):
    def __init__():
        super.__init__()

class Player(Mob):
    def __init__():
        super.__init__()

def get_all_player_names() -> list[str]:
    return [
        map_name.removesuffix(
            ".json"
        ) for map_name in os.listdir(
            "src/player"
        )
    ]
