if __name__ != "__main__":
    exit(0)

from typing import \
    Self,\
    NoReturn

try:
    import pygame
except ImportError:
    print("You need to install pygame to run this file.")
    print("On Windows, run \'py -m pip install pygame\'")
    print("On Mac/Linux, run \'python3 -m pip install pygame\'")
    exit(1)

try:
    from src.code.logger import \
        log            ,\
        log_success    ,\
        log_error      ,\
        log_fatal_error,\
        log_debug

    from src.code.loader import \
        WINDOW_SIZE,\
        FPS        ,\
        THEME      ,\
        TITLE      ,\
        COLOR
    
    from src.code.map import \
        Map     ,\
        load_map,\
        get_all_map_names

except Exception as e:
    print(e)
    print("You do not have the necessary modules in the correct directories.")
    pygame.quit(1)
    exit(1)
    
class Main:
    def proper_exit(
        self: Self,
        exit_code: int | None | str = 0
    ) -> NoReturn:
        pygame.quit()
        log_success(f"\'pygame\' quit")

        log_success(f"\'MAIN\' quit")
        log_success(f"ExitCode := {exit_code}")
        exit(exit_code)

    def set_state(
        self: Self,
        state: str
    ) -> None:
        self.state: str = state
        log_success(f"state set to: \'{state}\'")

    def update_theme(
        self: Self,
        theme: str
    ) -> None:
        THEME: str = theme
        match theme:
            case "dark":
                self.bg_color: pygame.color.Color = COLOR["gray31"]
            case "light":
                self.bg_color: pygame.color.Color = COLOR["gray3/4"]
            case _:
                log_fatal_error(
                    f"Invalid theme: {theme}"
                )
                self.proper_exit(1)

    def __init__(
        self: Self
    ) -> Self:
        self.WINDOW: pygame.Surface = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.set_state("main_menu")
        self.update_theme(THEME)
        log_debug(
            get_all_map_names(
                
            )
        )

    def handle_input(
        self: Self
    ) -> None | NoReturn:
        self.mouse_pos: tuple[int] = pygame.mouse.get_pos()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.proper_exit(0)
                
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.proper_exit(0)

                        case _: pass
                case _: pass

    def update(
        self: Self
    ) -> None:
        pass

    def render(
        self: Self
    ) -> None:
        self.WINDOW.fill(
            self.bg_color
        )
        

    def run(
        self: Self
    ) -> NoReturn:
        while True:
            self.dt: float = self.clock.tick(
                FPS
            )

            self.handle_input()
            self.update()
            self.render()

            pygame.display.update()

main: Main = Main()
main.run()
