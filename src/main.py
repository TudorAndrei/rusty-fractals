import numpy as np
from math import e as E
from fractals import JuliaSet, MandelbrotSet

from utils import get_pallette, paint
from viewport import Viewport

width, height = 1024, 1024
# width, height = 5, 5
channels = 3
image = np.ones((width, height, channels))
palette = get_pallette("gradient")

# mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=100)
# vp = Viewport(image, center=-0.75, width=3.5)

# mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)
# vp = Viewport(image, center=-0.7435 + 0.1314j, width=0.002)

mandelbrot_set = JuliaSet(
    max_iterations=20, escape_radius=1000, parameter=0.7885 * (E ** (0 + 1j))
)
vp = Viewport(image, center=-0.7435 + 0.1314j, width=5)
paint(mandelbrot_set, vp, palette, smooth=True, clamp=False)
vp.plot()
# print(vp.image)
