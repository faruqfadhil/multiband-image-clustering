from PIL import Image
import numpy as np
from numpy import zeros

warna1 = (255,255,255)
warna2 = (89,0,75)
data = []

im2 = Image.new("RGB", (32, 32))
pixels = im2.load()

for x in range(0, 32):
    for y in range(0, 32):
        pixels[x, y] = warna1
print(pixels)

# im2.show()

