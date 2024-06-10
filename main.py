if __name__ != "__main__":
    exit(0)

from typing import \
    Self    ,\
    NoReturn,\
    Any     ,\
    Callable
from types import \
    MethodType

import webbrowser

try:
    import pygame

except ImportError:
    print("You need to install pygame to run this file.")
    print("On Windows, run \'py -m pip install pygame\'")
    print("On Mac/Linux, run \'python3 -m pip install pygame\'")
    exit(1)
pygame.init()

try:
    from src.code.const import \
        ExitCode  ,\
        Coordinate,\
        Size

    from src.code.logger import \
        log            ,\
        log_success    ,\
        log_error      ,\
        log_fatal_error,\
        log_debug

    from src.code.loader import \
        load_json    ,\
                      \
        WINDOW_SIZE  ,\
        FPS          ,\
        THEME        ,\
                      \
        FIX_STGS     ,\
        TILE_SIZE    ,\
        TITLE        ,\
        RESOLUTIONS  ,\
        FPS_LIST     ,\
        CURSOR_LIST  ,\
        COLOR        ,\
        THEME_STYLE  ,\
        GUI_STGS     ,\
                      \
        FONT32       ,\
                      \
        load_image   ,\
                      \
        CURSOR_SIZE  ,\
        CURSOR_OFFSET,\
        CURSORS       \
    
    from src.code.button import \
        TextButton        ,\
        ImageButton       ,\
        ChangingTextButton,\
        get_buttons
    
    from src.code.map import \
        Map     ,\
        load_map,\
        get_all_map_names
    
    from src.code.text import \
        TextElement,\
        texts

except Exception as e:
    print(e)
    print("You do not have the necessary modules in the correct directories.")
    pygame.quit()
    exit(1)

try:
    # buttons[state][name]
    buttons: dict[str, dict[str, TextButton | ImageButton | ChangingTextButton]] = get_buttons(
        WINDOW_SIZE
    )

    # == MISC == #

    def __get_left_or_right_click__() -> int:
        """
        Return
            1 if left click released
            -1 if right click released
            0 otherwise
        """
        if pygame.mouse.get_just_released()[0]: return 1
        elif pygame.mouse.get_just_released()[2]: return -1
        else: return 0
    
    # == MAIN_MENU == #

    def __main_menu__singleplayer__(self: TextButton, *args, **kwargs) -> None: args[0].set_state("solo/player_selection")
    def __main_menu__multiplayer__ (self: TextButton, *args, **kwargs) -> None: args[0].set_state("multi/player_selection")
    def __main_menu__settings__    (self: TextButton, *args, **kwargs) -> None: args[0].set_state("settings")
    def __main_menu__credits__     (self: TextButton, *args, **kwargs) -> None: args[0].set_state("credits")
    def __main_menu__exit__        (self: TextButton, *args, **kwargs) -> NoReturn: args[0].proper_exit()
    def __main_menu__teaser__      (self: TextButton, *args, **kwargs) -> NoReturn:
        webbrowser.open('https://github.com/Schunche', new=2)
        args[0].proper_exit(0)

    # == SOLO / PLAYER_SELECTION == #
    
    #def __player_selection__back__(self: ImageButton, *args, **kwargs) -> None: args[0].set_state("main_menu")
    
    # == MULTI / PLAYER_SELECTION == #
    
    #def __player_selection__back__(self: ImageButton, *args, **kwargs) -> None: args[0].set_state("main_menu")

    # == SETTINGS == #

    # TODO on rightclick setting goes backwards
    # It should take up one more argument 
    # OR check for click type in function / extenal function / when the button push gets called

    def __settings__display_resolution__(self: ChangingTextButton, *args, **kwags) -> None:
        global RESOLUTIONS
        global WINDOW_SIZE

        if WINDOW_SIZE not in RESOLUTIONS:
            raise ValueError("Current WINDOW_SIZE is not in the allowed_display_resolutions dictionary.")
        
        WINDOW_SIZE = RESOLUTIONS[(RESOLUTIONS.index(WINDOW_SIZE) + __get_left_or_right_click__()) % len(RESOLUTIONS)]
        
        args[0].WINDOW = pygame.display.set_mode(
            WINDOW_SIZE,
            args[0].WINDOW.get_flags()
        )

    def __settings__fullscreen__(self: ChangingTextButton, *args, **kwags) -> None:
        global WINDOW_SIZE
        flags: int = args[0].WINDOW.get_flags()

        #fulls -> nofra -> border -> fulls...
        if __get_left_or_right_click__() == 1:
            if flags & pygame.FULLSCREEN: new_flags: int = pygame.NOFRAME
            elif flags & pygame.NOFRAME: new_flags: int = 0
            else: new_flags: int = pygame.FULLSCREEN
        else:
            if flags & pygame.FULLSCREEN: new_flags: int = 0
            elif flags & pygame.NOFRAME: new_flags: int = pygame.FULLSCREEN
            else: new_flags: int = pygame.NOFRAME
        
        args[0].WINDOW = pygame.display.set_mode(
            WINDOW_SIZE,
            new_flags
        )

    def __settings__fps__(self: ChangingTextButton, *args, **kwags) -> None:
        global FPS

        if FPS not in FPS_LIST:
            raise ValueError("The current FPS value is not in the FPS list.")

        FPS = FPS_LIST[(FPS_LIST.index(FPS) + __get_left_or_right_click__()) % len(FPS_LIST)]

    def __settings__theme__(self: ChangingTextButton, *args, **kwags) -> None:
        global THEME

        if THEME not in list(THEME_STYLE.keys()):
            raise ValueError("The current theme is not valid.")

        THEME = list(THEME_STYLE.keys())[(list(THEME_STYLE.keys()).index(THEME) + __get_left_or_right_click__()) % len(list(THEME_STYLE.keys()))]

    def __settings__cursor__(self: ChangingTextButton, *args, **kwags) -> None:

        if args[0].cursor_name not in CURSOR_LIST:
            raise ValueError("The current cursor is not valid.")

        # Set cursor to next on in the list
        args[0].cursor_name = CURSOR_LIST[(CURSOR_LIST.index(args[0].cursor_name) + __get_left_or_right_click__()) % len(CURSOR_LIST)]

    def __settings__back__(self: TextButton, *args, **kwargs) -> None: args[0].set_state("main_menu")

    # == RETURN == #

    def update_button_functionality() -> None:
        for state, butt in buttons.items():
            for name, button in butt.items():
                try:
                    exec(
                        f"button.push = MethodType(__{state}__{name}__, button)"
                    ) # https://stackoverflow.com/questions/394770/override-a-method-at-instance-level
                except:
                    log_error(
                        f"couldn\'t execute expression: button.push = MethodType(__{state}__{name}__, button)"
                    )
    
    update_button_functionality()
    
except:
    log_fatal_error(
        "Something ain\'t working at \'button.push()\' re-assigns"
    )
    exit(1)

class Main:
    def proper_exit(
        self: Self,
        exit_code: ExitCode = 0
    ) -> NoReturn:
        pygame.quit()
        log_success(f"\'pygame\' quit")

        log_success(f"\'MAIN\' quit")
        log_success(f"ExitCode: {exit_code}")
        exit(exit_code)

    def set_state(
        self: Self,
        state: str
    ) -> None:
        self.state: str = state
        log_success(f"state set to: \'{state}\'")

    def __init__(
        self: Self
    ) -> Self:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.WINDOW: pygame.Surface = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(load_image("logo/icon"))
        self.cursor_name: None | str = None
        self.set_state("main_menu")

    def handle_input(
        self: Self
    ) -> None | NoReturn:
        self.mouse_pos: Coordinate = pygame.mouse.get_pos()

        for event in pygame.event.get():
            das_event = pygame.constants.__dict__
            event_name = list(das_event.keys())[list(das_event.values()).index(event.type)]
            #log_debug(f"{event_name}: {event.type}")

            if event.type == pygame.QUIT:
                    self.proper_exit(0)

            if event.type == pygame.WINDOWSIZECHANGED:
                global buttons
                buttons = get_buttons(
                    WINDOW_SIZE
                )
                update_button_functionality()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or \
                (event.button == 3 and self.state == "settings"):
                    for name, button in buttons[self.state].items():
                        if button.inner_rect.collidepoint(self.mouse_pos):
                            button.push(self)
                            self.handle_input()
                            break
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "main_menu":
                        self.proper_exit(0)
                    elif self.state in [
                        "player_selection",
                        "settings",
                        "credits"
                    ]:
                        self.set_state("main_menu")

                if event.key == pygame.K_F11:
                    if pygame.FULLSCREEN & self.WINDOW.get_flags():
                        self.WINDOW: pygame.Surface = pygame.display.set_mode(self.WINDOW.get_size())
                    else:
                        self.WINDOW: pygame.Surface = pygame.display.set_mode(self.WINDOW.get_size(), flags=pygame.FULLSCREEN)

    def update(
        self: Self
    ) -> None:
        pass

    def render(
        self: Self,
        debug: bool = False
    ) -> None:
        # == ACTUAL RENDER == #
        self.WINDOW.fill(
            COLOR[THEME_STYLE[THEME]["background"]]
        )

        for name in texts[self.state].keys():
            text = texts[self.state][name][THEME]
            text.render(
                self.WINDOW
            )

        for name, button in buttons[self.state].items():
            if isinstance(button, ChangingTextButton) and self.state == "settings":
                if name == "display_resolution":
                    resolution_key: str = [
                        key for key, resolution in FIX_STGS["window"]["allowed_display_resolutions"].items() if resolution == WINDOW_SIZE
                    ][0]

                    button.render(
                        self.WINDOW,
                        self.mouse_pos,
                        THEME,
                        f"{resolution_key}: " + ", ".join([f"{side}px" for side in WINDOW_SIZE])
                    )

                elif name == "fullscreen":
                    flags: int = self.WINDOW.get_flags()
                    if flags & pygame.FULLSCREEN: msg: str = "Fullscreen"
                    elif flags & pygame.NOFRAME: msg: str = "Windowed Borderless"
                    else: msg: str = "Windowed"

                    button.render(
                        self.WINDOW,
                        self.mouse_pos,
                        THEME,
                        msg
                    )

                elif name == "fps":
                    button.render(
                        self.WINDOW,
                        self.mouse_pos,
                        THEME,
                        f"{FPS} FPS"
                    )

                elif name == "theme":
                    button.render(
                        self.WINDOW,
                        self.mouse_pos,
                        THEME,
                        THEME.title()
                    )

                elif name == "cursor":
                    button.render(
                        self.WINDOW,
                        self.mouse_pos,
                        THEME,
                        ("Cursor style: " + (str(self.cursor_name) if self.cursor_name is not None else f"System")).title()
                    )

            else:
                button.render(
                    self.WINDOW,
                    self.mouse_pos,
                    THEME
                )

        # == HOVER EFFECT == #
        for name, button in buttons[self.state].items():
            if button.inner_rect.collidepoint(self.mouse_pos):
                if self.cursor_name is None:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif self.cursor_name == "pygame #1":
                    pygame.mouse.set_cursor(pygame.cursors.ball)
                elif self.cursor_name == "pygame #2":
                    pygame.mouse.set_cursor(pygame.cursors.tri_right)
                else:
                    pygame.mouse.set_cursor(
                        CURSOR_SIZE,
                        CURSOR_OFFSET[self.cursor_name]["hand"],
                        *CURSORS[self.cursor_name]["hand"]
                    )
                
                break
        else:
            if self.cursor_name is None:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            elif self.cursor_name == "pygame #1":
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
            elif self.cursor_name == "pygame #2":
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            else:
                pygame.mouse.set_cursor(
                    CURSOR_SIZE,
                    CURSOR_OFFSET[self.cursor_name]["arrow"],
                    *CURSORS[self.cursor_name]["arrow"]
                )

        # == DEBUG RENDER == #
        if debug:
            fps_text_rendered: pygame.Surface = FONT32.render(
                f"FPS: {1 / self.dt:.2f}",
                False,
                COLOR[THEME_STYLE[THEME]["debug_text_color"]]
            )
            fps_text_rect: pygame.Rect = fps_text_rendered.get_rect(
                topleft=(
                    GUI_STGS["global"]["outer_padding"],
                    GUI_STGS["global"]["outer_padding"]
                )
            )
            self.WINDOW.blit(
                fps_text_rendered,
                fps_text_rect
            )

    def run(
        self: Self
    ) -> NoReturn:
        while True:
            self.dt: float = self.clock.tick(
                FPS
            ) * 0.001

            self.handle_input()
            self.update()
            self.render()
            
            pygame.display.update()

main: Main = Main()
main.run()
