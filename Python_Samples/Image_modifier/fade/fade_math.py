from math import *

def dist(pixel_r, pixel_c, row, col):
        return sqrt((row - pixel_r) ** 2 +
                    (col - pixel_c) ** 2)

def fade_scale_val(radius, distance):
        return max(((radius - distance) / radius), 0.2)
