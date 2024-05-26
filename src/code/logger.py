"""
Import this module.
"""

# I assume the module 'time' can always be imported without an error
import time

class ColorTerminal:
    """
    Class solely for applying ANSI color codes to text in the terminal.
    Used for logging, debugging.
    """

    color_codes: dict[str, str] = {
        'reset':          '\033[0m',
        'bold':           '\033[01m',
        'disabled':       '\033[02m',
        'underline':      '\033[04m',
        'reverse':        '\033[07m',
        'strike_through': '\033[09m',
        'invisible':      '\033[08m',
        
        'fg_black':       '\033[30m',
        'fg_red':         '\033[31m',
        'fg_green':       '\033[32m',
        'fg_orange':      '\033[33m',
        'fg_blue':        '\033[34m',
        'fg_purple':      '\033[35m',
        'fg_cyan':        '\033[36m',
        'fg_light_grey':  '\033[37m',
        'fg_dark_grey':   '\033[90m',
        'fg_light_red':   '\033[91m',
        'fg_light_green': '\033[92m',
        'fg_yellow':      '\033[93m',
        'fg_light_blue':  '\033[94m',
        'fg_pink':        '\033[95m',
        'fg_light_cyan':  '\033[96m',
        
        'bg_black':       '\033[40m',
        'bg_red':         '\033[41m',
        'bg_green':       '\033[42m',
        'bg_orange':      '\033[43m',
        'bg_blue':        '\033[44m',
        'bg_purple':      '\033[45m',
        'bg_cyan':        '\033[46m',
        'bg_light_grey':  '\033[47m'
    }

    @classmethod
    def apply(cls, text: str, *styles: str) -> str:
        """
        Apply color to the given text.

        Args:
            text (str): The text to colorize.
            styles (str, any number of them): The name of the color/style to apply.

        Returns:
            str: The colorized text.
        """
        apply_style: str = ""
        for style in styles:
            try:
                apply_style += cls.color_codes[style]
            except KeyError:
                print(f"{cls.color_codes['reset']}{cls.color_codes['bg_red']}Unknown style: {style}{cls.color_codes['reset']}")

        return f"{cls.color_codes['reset']}{apply_style}{text}{cls.color_codes['reset']}"

def log(
    text: str,
    *styles: str,
    only_text: bool = True
) -> None:
    if styles != ():
        if only_text:
            print(f"{time.asctime()} :> {ColorTerminal.apply(f'{text}', *styles)}")
        else:
            print(ColorTerminal.apply(f"{time.asctime()} :> {text}", *styles))
    else:
        print(f"{time.asctime()} :> {text}")

def log_fatal_error(
    text
) -> None:
    log(
        text,
        "bg_red",
        "fg_black",
        only_text=False
    )

def log_error(
    text
) -> None:
    log(
        text,
        "bg_red",
        "fg_black"
    )

def log_success(
    text
) -> None:
    log(
        text,
        "bg_green",
        "fg_black"
    )

def log_debug(
    text
) -> None:
    log(
        text,
        "bg_blue",
        "bold",
        "fg_black"
    )