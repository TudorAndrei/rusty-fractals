from scipy.interpolate import interp1d
from matplotlib import colormaps
import numpy as np


def paint(set_, viewport, palette, smooth, clamp=True):
    for pixel in viewport:
        stability = set_.stability(complex(pixel), smooth=smooth, clamp=clamp)
        index = int(min(stability * len(palette), len(palette) - 1))
        # print(index)
        pixel.color = palette[index % len(palette)]
    # return viewport.image


def denormalize(palette):
    return [tuple(int(channel * 255) for channel in color) for color in palette]


def make_gradient(colors, interpolation="linear"):
    X = [i / (len(colors) - 1) for i in range(len(colors))]
    Y = [[color[i] for color in colors] for i in range(3)]
    channels = [interp1d(X, y, kind=interpolation) for y in Y]
    return lambda x: [np.clip(channel(x), 0, 1) for channel in channels]


def get_pallette(mode: str):
    if mode == "gradient":
        black = (0, 0, 0)
        blue = (0, 0, 1)
        maroon = (0.5, 0, 0)
        navy = (0, 0, 0.5)
        red = (1, 0, 0)

        colors = [black, navy, blue, maroon, red, black]
        gradient = make_gradient(colors, interpolation="cubic")
        num_colors = 256
        palette = denormalize([gradient(i / num_colors) for i in range(num_colors)])
        return palette
    elif mode == "cmap":
        cmap = "twilight"
        colormap = colormaps.get_cmap(cmap).colors
        palette = denormalize(colormap)


if __name__ == "__main__":
    cmap = "twilight"
    colormap = colormaps.get_cmap(cmap).colors
    print(len(colormap))
