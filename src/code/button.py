from typing import \
    Self,\
    Any

import pygame

from src.code.const import \
    Coordinate,\
    Size
from src.code.logger import \
    log_error,\
    log_fatal_error
from src.code.loader import \
    FIX_STGS       ,\
    COLOR          ,\
    THEME_STYLE    ,\
    GUI_STGS       ,\
    GLOBAL_GUI_STGS,\
                    \
    FONT32         ,\
    load_image

BUTTON_STGS: dict[str] = GUI_STGS["button"]

class TextButton:
    def __init__(
        self: Self,
        text: str,
        pos: Coordinate,
        size: Size,
        *tags: str,
        align: str = "topleft"
    ) -> None:
        self.inner_rect: pygame.Rect = pygame.Rect(
            *pos, *size
        )
        try:
            exec(
                f"self.inner_rect.{align}: Coordinate = pos"
            )
        except:
            log_fatal_error(
                f"There is no such align as: {align}"
            )
            exit(1)
        
        self.border_rect: pygame.Rect = pygame.Rect(
            pos[0] - BUTTON_STGS["border_width"] * 0.5,
            pos[1] - BUTTON_STGS["border_width"] * 0.5,
            size[0] + BUTTON_STGS["border_width"],
            size[1] + BUTTON_STGS["border_width"]
        )

        match align:
            case "topleft":
                pass
            case "center":
                self.border_rect.center = pos
            case _:
                if align in [
                    "topleft", "topright", "bottomleft", "bottomright",
                    "midtop", "midleft", "midright", "midbottom",
                    "center", "size"
                    # size is a bit odd,
                    # but I accept it,
                    # as it is a tuple
                    # containing two numbers
                ]:
                    log_error(
                        f"Button align not implemented yet: Make this bro (literally 6 lines of code)"
                    )
                    exit(1)
                else:
                    log_fatal_error(
                        f"There is no such align as: {align}"
                    )
                    exit(1)
        
        self.text_renders: dict[str, pygame.Surface] = {
            theme: FONT32.render(
                text,
                True,
                COLOR[colors["button_text_color"]]
            ) for theme, colors in THEME_STYLE.items()
        }
        self.text_rect: pygame.Rect = self.text_renders["dark"].get_rect(
            center=(
                self.inner_rect.center
            )
        )

    def push(
        self: Self,
        *args: Any,
        **kwargs: Any
    ) -> None:
        log_fatal_error("Not implemented button functionality")
        exit(1)

    def render(
        self: Self,
        surface: pygame.Surface,
        mouse_pos: Coordinate,
        theme: str
    ) -> None:
        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_bg_color" \
                if not self.inner_rect.collidepoint(*mouse_pos) else \
                "button_hover_color"]],
            self.inner_rect
        )

        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_border_color"]],
            self.border_rect,
            BUTTON_STGS["border_width"],
            BUTTON_STGS["border_radius"]
        )

        surface.blit(
            self.text_renders[theme],
            self.text_rect
        )

class ImageButton:
    def __init__(
        self: Self,
        image: pygame.Surface,
        pos: Coordinate,
        size: Size,
        *tags: str,
        align: str = "topleft",
        fill: bool = True
    ) -> None:
        self.inner_rect: pygame.Rect = pygame.Rect(
            *pos, *size
        )
        try:
            exec(
                f"self.inner_rect.{align}: Coordinate = pos"
            )
        except:
            log_fatal_error(
                f"There is no such align as: {align}"
            )
            exit(1)
        
        self.border_rect: pygame.Rect = pygame.Rect(
            pos[0] - BUTTON_STGS["border_width"] * 0.5,
            pos[1] - BUTTON_STGS["border_width"] * 0.5,
            size[0] + BUTTON_STGS["border_width"],
            size[1] + BUTTON_STGS["border_width"]
        )

        match align:
            case "topleft":
                pass
            case "center":
                self.border_rect.center = pos
            case _:
                if align in [
                    "topleft", "topright", "bottomleft", "bottomright",
                    "midtop", "midleft", "midright", "midbottom",
                    "center", "size"
                    # size is a bit odd,
                    # but I accept it,
                    # as it is a tuple
                    # containing two numbers
                ]:
                    log_error(
                        f"Button align not implemented yet: Make this bro (literally 6 lines of code)"
                    )
                    exit(1)
                else:
                    log_fatal_error(
                        f"There is no such align as: {align}"
                    )
                    exit(1)

        self.image: pygame.Surface = image
        if fill:
            pass #TODO
        else:
            self.image_pos: Coordinate = self.inner_rect.topleft

    def push(
        self: Self,
        *args: Any,
        **kwargs: Any
    ) -> None:
        log_fatal_error("Not implemented button functionality")
        exit(1)

    def render(
        self: Self,
        surface: pygame.Surface,
        mouse_pos: Coordinate,
        theme: str
    ) -> None:
        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_bg_color" #\
                #if not self.inner_rect.collidepoint(*mouse_pos) else \
                #"button_hover_color"
            ]],
            self.inner_rect
        )

        surface.blit(
            self.image,
            self.image_pos
        )

        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_border_color"]],
            self.border_rect,
            BUTTON_STGS["border_width"],
            BUTTON_STGS["border_radius"]
        )

class ChangingTextButton:
    def __init__(
        self: Self,
        pos: Coordinate,
        size: Size,
        *tags: str,
        align: str = "topleft"
    ) -> None:
        self.inner_rect: pygame.Rect = pygame.Rect(
            *pos, *size
        )
        try:
            exec(
                f"self.inner_rect.{align}: Coordinate = pos"
            )
        except:
            log_fatal_error(
                f"There is no such align as: {align}"
            )
            exit(1)
        
        self.border_rect: pygame.Rect = pygame.Rect(
            pos[0] - BUTTON_STGS["border_width"] * 0.5,
            pos[1] - BUTTON_STGS["border_width"] * 0.5,
            size[0] + BUTTON_STGS["border_width"],
            size[1] + BUTTON_STGS["border_width"]
        )

        match align:
            case "topleft":
                pass
            case "center":
                self.border_rect.center = pos
            case _:
                if align in [
                    "topleft", "topright", "bottomleft", "bottomright",
                    "midtop", "midleft", "midright", "midbottom",
                    "center", "size"
                    # size is a bit odd,
                    # but I accept it,
                    # as it is a tuple
                    # containing two numbers
                ]:
                    log_error(
                        f"Button align not implemented yet: Make this bro (literally 6 lines of code)"
                    )
                    exit(1)
                else:
                    log_fatal_error(
                        f"There is no such align as: {align}"
                    )
                    exit(1)

    def push(
        self: Self,
        that,
        *args: Any,
        **kwargs: Any
    ) -> None:
        log_fatal_error("Not implemented button functionality")
        exit(1)

    def render(
        self: Self,
        surface: pygame.Surface,
        mouse_pos: Coordinate,
        theme: str,
        text: str
    ) -> None:
        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_bg_color" \
                if not self.inner_rect.collidepoint(*mouse_pos) else \
                "button_hover_color"]],
            self.inner_rect
        )

        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_border_color"]],
            self.border_rect,
            BUTTON_STGS["border_width"],
            BUTTON_STGS["border_radius"]
        )

        self.text_rendered: pygame.Surface = FONT32.render(
            text,
            True,
            COLOR[THEME_STYLE[theme]["button_text_color"]]
        )
        self.text_rect: pygame.Rect = self.text_rendered.get_rect(
            center=(
                self.inner_rect.center
            )
        )

        surface.blit(
            self.text_rendered,
            self.text_rect
        )

class PlayerSelectionButton:
    def __init__(
        self: Self,
        pos: Coordinate,
        size: Size,
        *tags: str,
        align: str = "topleft"
    ) -> None:
        self.inner_rect: pygame.Rect = pygame.Rect(
            *pos, *size
        )
        try:
            exec(
                f"self.inner_rect.{align}: Coordinate = pos"
            )
        except:
            log_fatal_error(
                f"There is no such align as: {align}"
            )
            exit(1)
        
        self.border_rect: pygame.Rect = pygame.Rect(
            pos[0] - BUTTON_STGS["border_width"] * 0.5,
            pos[1] - BUTTON_STGS["border_width"] * 0.5,
            size[0] + BUTTON_STGS["border_width"],
            size[1] + BUTTON_STGS["border_width"]
        )

        match align:
            case "topleft":
                pass
            case "center":
                self.border_rect.center = pos
            case _:
                if align in [
                    "topleft", "topright", "bottomleft", "bottomright",
                    "midtop", "midleft", "midright", "midbottom",
                    "center", "size"
                    # size is a bit odd,
                    # but I accept it,
                    # as it is a tuple
                    # containing two numbers
                ]:
                    log_error(
                        f"Button align not implemented yet: Make this bro (literally 6 lines of code)"
                    )
                    exit(1)
                else:
                    log_fatal_error(
                        f"There is no such align as: {align}"
                    )
                    exit(1)

    def push(
        self: Self,
        that,
        *args: Any,
        **kwargs: Any
    ) -> None:
        log_fatal_error("Not implemented button functionality")
        exit(1)

    def render(
        self: Self,
        surface: pygame.Surface,
        mouse_pos: Coordinate,
        theme: str,
        text: str
    ) -> None:
        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_bg_color" \
                if not self.inner_rect.collidepoint(*mouse_pos) else \
                "button_hover_color"]],
            self.inner_rect
        )

        pygame.draw.rect(
            surface,
            COLOR[THEME_STYLE[theme]["button_border_color"]],
            self.border_rect,
            BUTTON_STGS["border_width"],
            BUTTON_STGS["border_radius"]
        )

        self.text_rendered: pygame.Surface = FONT32.render(
            text,
            True,
            COLOR[THEME_STYLE[theme]["button_text_color"]]
        )
        self.text_rect: pygame.Rect = self.text_rendered.get_rect(
            center=(
                self.inner_rect.center
            )
        )

        surface.blit(
            self.text_rendered,
            self.text_rect
        )

def get_buttons(
    window_size: Size
) -> dict[str, dict[str, TextButton | ImageButton | ChangingTextButton]]:
    buttons_: dict[str, dict[str, TextButton | ImageButton | ChangingTextButton]] = {}

    # == MAIN_MENU == # APPLICABLE | EXPANDABLE
    num: int = 5
    button_height: int = int(
        (window_size[1] - (num - 1) * GLOBAL_GUI_STGS["element_interval"] - 2 * GLOBAL_GUI_STGS["outer_padding"]) / num
    )
    o_teaser: pygame.Surface = load_image("logo/mainteaser")
    n_teaser_h: int = window_size[1] - 2 * GLOBAL_GUI_STGS["outer_padding"]
    teaser_new: pygame.Surface = pygame.transform.scale(
        o_teaser, (
            int(o_teaser.get_width() * n_teaser_h / o_teaser.get_height()),
            n_teaser_h
        )
    )
    button_width: int = window_size[0] - 2 * GLOBAL_GUI_STGS["outer_padding"] - teaser_new.get_width() - GLOBAL_GUI_STGS["element_interval"]

    # ==>
    buttons_["main_menu"] = {
        # COL 1
        "singleplayer": TextButton("Singleplayer",
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"]),
            (button_width, button_height)
        ),"multiplayer": TextButton("Multiplayer",
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"]),
            (button_width, button_height)
        ), "settings": TextButton("Settings",
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"] + 1 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        ), "credits": TextButton("Credits",
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"] + 2 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        ), "exit": TextButton("Exit",
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"] + 3 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        ),
        # MAIN IMAGE
        "teaser": ImageButton(teaser_new, (
                GLOBAL_GUI_STGS["outer_padding"] + button_width + GLOBAL_GUI_STGS["element_interval"],
                GLOBAL_GUI_STGS["outer_padding"]
            ), teaser_new.get_size(),
            fill=False
        )
    }

    # == SETTINGS == # APPLICABLE | EXTENDABLE
    rows: int = 3
    cols: int = 3

    button_width: int = int((window_size[0] - 2 * GLOBAL_GUI_STGS["outer_padding"] - (cols - 1) * GLOBAL_GUI_STGS["element_interval"]) / cols)
    button_height: int = int((window_size[1] - 2 * GLOBAL_GUI_STGS["outer_padding"] - (rows - 1) * GLOBAL_GUI_STGS["element_interval"]) / rows)

    # ==>
    buttons_["settings"] = {
        # ROW 1
        "display_resolution": ChangingTextButton(
            (GLOBAL_GUI_STGS["outer_padding"], GLOBAL_GUI_STGS["outer_padding"]),
            (button_width, button_height)
        ), "fullscreen": ChangingTextButton(
            (GLOBAL_GUI_STGS["outer_padding"] + 1 * (button_width + GLOBAL_GUI_STGS["element_interval"]),
            GLOBAL_GUI_STGS["outer_padding"]),
            (button_width, button_height)
        ), "fps": ChangingTextButton(
            (GLOBAL_GUI_STGS["outer_padding"] + 2 * (button_width + GLOBAL_GUI_STGS["element_interval"]),
            GLOBAL_GUI_STGS["outer_padding"]),
            (button_width, button_height)
        ),
        # ROW 2
        "theme": ChangingTextButton(
            (GLOBAL_GUI_STGS["outer_padding"],
            GLOBAL_GUI_STGS["outer_padding"]  + 1 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        ), "cursor": ChangingTextButton(
            (GLOBAL_GUI_STGS["outer_padding"] + 1 * (button_width + GLOBAL_GUI_STGS["element_interval"]),
            GLOBAL_GUI_STGS["outer_padding"]  + 1 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        ), "back": TextButton("Back",
            (GLOBAL_GUI_STGS["outer_padding"] + 2 * (button_width + GLOBAL_GUI_STGS["element_interval"]),
            GLOBAL_GUI_STGS["outer_padding"]  + 1 * (button_height + GLOBAL_GUI_STGS["element_interval"])),
            (button_width, button_height)
        )
    }

    # == CREDITS == # TODO

    # ==>
    buttons_["credits"] = {}

    # == SOLO / PLAYER_SELECTION == # TODO
    

    # SOLO ==>
    buttons_["solo/player_selection"] = {}

    # MULTI ==>
    buttons_["multi/player_selection"] = {}

    # == RETURN == # APPLICABLE
    #buttons_[state][alias] = Button
    return buttons_
