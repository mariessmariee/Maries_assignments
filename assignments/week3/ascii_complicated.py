import random

import time, random, math

def ask_int_in_range(prompt, lo, hi):
    while True:
        s = input(f"{prompt} [{lo}-{hi}]: ").strip()
        try:
            v = int(s)
            if lo <= v <= hi:
                return v
            print(f"Please enter a number between {lo} and {hi}.")
        except ValueError:
            print("Please enter a valid integer.")

def ask_symbol(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s[0]
        print("Please enter at least one character.")

height = ask_int_in_range("Heart tile height", 5, 20)
width = ask_int_in_range("Heart tile width", 7, 35)
symbol = ask_symbol("Enter a cute symbol (e.g., ❤, ✨, *, +): ")

background_pool_basic = ['.', '`', ' ', '*', '+']
background_pool_spark = ['.', '*', '+']

theme = input("Theme (classic/sparkle): ").strip().lower()
if theme not in {"classic", "sparkle"}:
    theme = "classic"

def make_heart_tile(h, w, fill, theme):
    tile = []
    for r in range(h):
        row_chars = []
        y = 1.3 - 2.6 * (r / (h - 1))
        for c in range(w):
            x = -1.3 + 2.6 * (c / (w - 1))
            inside = (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0
            if inside:
                row_chars.append(fill)
            else:
                if theme == "sparkle":
                    row_chars.append(random.choice(background_pool_spark))
                else:
                    row_chars.append(random.choice(background_pool_basic))
        tile.append("".join(row_chars))
    return tile

tile = make_heart_tile(height, width, symbol, theme)

repeat_x = ask_int_in_range("How many hearts across", 1, 5)
repeat_y = ask_int_in_range("How many hearts down", 1, 5)

for _ in range(repeat_y):
    for row in tile:
        print(("  ".join([row] * repeat_x)))
        time.sleep(0.1)
    print()