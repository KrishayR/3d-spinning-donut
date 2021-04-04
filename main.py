import pygame as pg
import math
import colorsys

pg.init()

orange = (255, 114, 54)
black = (0, 0, 0)
hue = 0

width = 1000
height = 1000

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = height // y_separator
columns = width // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 3

chars = ".,-~:;=!*#$@"

screen = pg.display.set_mode((width, height))

display_surface = pg.display.set_mode((width, height))

pg.display.set_caption('3d spinning donut')
font = pg.font.SysFont('Arial', 18, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))


run = True
while run:

    screen.fill((black))

    z = [0] * screen_size
    b = [' '] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00002
        B += 0.00001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator


    pg.display.update()

    hue += 0.005

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
