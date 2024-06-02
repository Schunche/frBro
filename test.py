import pygame
import os

for cursor_style in os.listdir("src/data/cursor"):
    print(
        os.listdir(
            f"src/data/cursor/{cursor_style}"
        )
    )

