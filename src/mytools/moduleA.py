
# < ======================================================================================================
# < Imports
# < ======================================================================================================

import random

# < ======================================================================================================
# < Functions
# < ======================================================================================================

def cprint(content: any, rgb: tuple[int, int, int] | None = None, end = "\n"):
    """Print rgb colour text to compatible terminals, picks a random colour if one is not provided"""
    rgb: tuple[int, int, int] = [random.randint(32,255) for _ in range(3)] if rgb == None else rgb
    text: str = str(content)
    code: str = f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m'
    reset: str = '\033[39m'
    print(f"{code}{text}{reset}", end = end)