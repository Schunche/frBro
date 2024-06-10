if __name__ == "__main__":
    exit(0)

from typing import \
    Self

import pygame

from src.code.const import \
    Coordinate
from src.code.loader import \
    COLOR          ,\
    THEME_STYLE    ,\
    GLOBAL_GUI_STGS,\
    FONT32

class TextElement:
    def __init__(
        self: Self,
        theme: str,
        text: str,
        font: pygame.font.Font,
        pos: Coordinate,
        align: str = "topleft"
    ) -> None:
        self.text_rendered: pygame.Surface = font.render(
            text,
            False,
            COLOR[THEME_STYLE[theme]["button_text_color"]]
        )
        exec(
            f"self.text_rect: pygame.Rect = self.text_rendered.get_rect({align}=pos)"
        )
    
    def render(
        self: Self,
        surface: pygame.Surface
    ) -> None:
        surface.blit(
            self.text_rendered,
            self.text_rect
        )

def get_texts() -> dict[str, dict[str, dict[str, TextElement]]]:
    # texts[state][name][theme]
    texts_: dict[str, dict[str, dict[str, TextElement]]] = {
        "main_menu": {

        }, "credits": {
            "author": {},
            "cmd": {}
        }, "settings": {

        }, "player_selection": {

        }
    }
    themes: list[str] = list(THEME_STYLE.keys())

    # == CREDITS == #
    for theme in themes:
        texts_["credits"]["author"][theme] = TextElement(
            theme,
            "Author: Schunche",
            FONT32, (
                GLOBAL_GUI_STGS["outer_padding"],
                GLOBAL_GUI_STGS["outer_padding"]
            )
        )
        surface_: pygame.Surface = pygame.Surface((720, 200), pygame.SRCALPHA)
        FONT32.set_bold(True)
        FONT32.set_underline(True)
        surface_.blit(
            FONT32.render(
                "Author", True, COLOR[THEME_STYLE[theme]["button_text_color"]]
            ), (0, 0)
        )
        size_ = FONT32.size("Author")
        FONT32.set_bold(False)
        FONT32.set_underline(False)
        surface_.blit(
            FONT32.render(
                ": Schunche", True, COLOR[THEME_STYLE[theme]["button_text_color"]]
            ), (size_[0], 0)
        )
        texts_["credits"]["author"][theme].text_rendered = surface_
        texts_["credits"]["author"][theme].text_rect = pygame.Rect(
            texts_["credits"]["author"][theme].text_rect.x,
            texts_["credits"]["author"][theme].text_rect.y,
            *texts_["credits"]["author"][theme].text_rendered.size
        )

        # =================================================================================================== #
        
        texts_["credits"]["cmd"][theme] = TextElement(
            theme,
            "Inspiration: Clear Code, DaFluffyPotato, Squanto",
            FONT32, (
                GLOBAL_GUI_STGS["outer_padding"],
                GLOBAL_GUI_STGS["outer_padding"] + FONT32.size("Inspiration")[1]
            )
        )
        surface_: pygame.Surface = pygame.Surface((720, 200), pygame.SRCALPHA)
        FONT32.set_bold(True)
        surface_.blit(
            FONT32.render(
                "Inspiration", True, COLOR[THEME_STYLE[theme]["button_text_color"]]
            ), (0, 0)
        )
        size_ = FONT32.size("Inspiration")
        FONT32.set_bold(False)
        surface_.blit(
            FONT32.render(
                ": Clear Code, DaFluffyPotato, Squanto", True, COLOR[THEME_STYLE[theme]["button_text_color"]]
            ), (size_[0], 0)
        )
        texts_["credits"]["cmd"][theme].text_rendered = surface_
        texts_["credits"]["cmd"][theme].text_rect = pygame.Rect(
            texts_["credits"]["cmd"][theme].text_rect.x,
            texts_["credits"]["cmd"][theme].text_rect.y,
            *texts_["credits"]["cmd"][theme].text_rendered.size
        )

    # == RETURN == #
    del themes

    return texts_

texts: dict[str, dict[str, dict[str, TextElement]]] = get_texts()
