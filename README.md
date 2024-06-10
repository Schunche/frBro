# [frBro](https://github.com/Schunche/frBro)
## 2024. 05. 26.
<h3>
    File system:
</h3>
<ul>
    <li>
        <p>
            <b>
                const.py
            </b>
        </p>
        <p>
            Contains global type aliases.
        </p>
    </li>
    <li>
        <p>
            <b>
                logger.py
            </b>
        </p>
        <p>
            Logs information to console/terminal.
        </p>
    </li>
    <li>
        <p>
            <b>
                loader.py
            </b>
        </p>
        <p>
            Helps with loading json and png files.
        </p>
        <p>
            Dependencies:
        </p>
        <ul>
            <li>
                const.py
            </li>
            <li>
                logger.py
            </li>
        </ul>
    </li>
    <li>
        <p>
            <b>
                map.py
            </b>
        </p>
        <p>
            Helps with loading json and png files.
        </p>
        <p>
            Dependencies:
        </p>
        <ul>
            <li>
                const.py
            </li>
            <li>
                logger.py
            </li>
        </ul>
    </li>
</ul>

## 2024. 05. 30
#### Note: dict.keys() and dict.values() are not lists.
#### Button types:

1. given text, that does not change, with hover effect
2. changing text, that does change, with hover effect
3. image, that does not change, without hover effect

## 2024. 06. 02.
#### Built-in cursors

- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)     # normal cursor
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)      # normal hand with finger
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)     # text selection bar

- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)        # negation sign
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR) # +

- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)   # resize +
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENESW)  # resize /
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)    # resize |
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)  # resize \
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)    # resize -

- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)      # load anim circle # 1
- pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW) # load anim circle # 2

**pygame *ready* cursors**

- pygame.cursors.arrow     # inverted normal arrow

- pygame.cursors.ball      # just a black ball & center is the hotspot
- pygame.cursors.broken_x  # a shooter like "X", with the center being a hole, again, inverted
- pygame.cursors.diamond   # a 45^ degree rotated square, with itself in the center (donut-like)

- pygame.cursors.tri_left  # a thing, i have almost created
- pygame.cursors.tri_right # a thing, i have almost created, revered along the y axis

**Currently using:**
- pygame.SYSTEM_CURSOR_ARROW # normal cursor
- pygame.SYSTEM_CURSOR_HAND  # normal hand with finger

## 2024. 06. 07. - [multi-demo](https://github.com/Schunche/multi-demo) - Project started
I have a fairly okay menu system, i started this secondary project to learn how to send data between different computers.

## 2024. 06. 10.

Trying to connect [this project](https://github.com/Schunche/frBro) with the [networking one](https://github.com/Schunche/multi-demo)
