from typing import \
    TypeAlias

ExitCode: TypeAlias = (int | None | str)

Coordinate: TypeAlias = tuple[int, int]
Tile: TypeAlias = dict[str, str | int]
Size: TypeAlias = list[int, int]

JsonReturn: TypeAlias = (dict | list | None | bool | int | float | str)
