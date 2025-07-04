import random
import time

height = int(input("Enter the height of the heart tile (suggest 5-10): "))
width = int(input("Enter the width of the heart tile (suggest 5-10): "))
symbol = input("Enter a cute symbol (like ❤️, 💖, ✨, 🌸, or just *): ")

background_choices = ['.', '･ﾟ', ' ', '*', '`']

if symbol == "💖":
    background_choices = ['✨', '🌟', '🦄', '💫']

def create_tile(h, w, symbol):
    tile = []
    for row in range(h):
        line = ""
        for col in range(w):
            if (row == 0 and (col == 1 or col == w-2)) or \
               (row == 1 and (col == 0 or col == 2 or col == w-3 or col == w-1)) or \
               (row == 2 and (col == 1 or col == w-2)) or \
               (row == 3 and (col == 2 or col == w-3)) or \
               (row == 4 and (col == w//2)):
                line += symbol
            else:
                line += random.choice(background_choices)
        tile.append(line)
    return tile

tile = create_tile(height, width, symbol)

repeat_x = int(input("How many hearts across? (2-5 suggested): "))
repeat_y = int(input("How many hearts down? (2-5 suggested): "))

for y in range(repeat_y):
    for row in tile:
        for x in range(repeat_x):
            print(row, end="  ")
        print()
        time.sleep(0.1)
    print()
