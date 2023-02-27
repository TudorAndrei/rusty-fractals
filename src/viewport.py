from dataclasses import dataclass
import cv2
import matplotlib.pyplot as plt

from numpy.typing import NDArray


@dataclass
class Viewport:
    image: NDArray
    center: complex
    width: float

    @property
    def height(self):
        return self.scale * self.image.shape[0]

    @property
    def offset(self):
        return self.center + complex(-self.width, self.height) / 2

    @property
    def scale(self):
        return self.width / self.image.shape[1]

    def __iter__(self):
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                yield Pixel(self, x, y)

    def plot(self, cmap=None):
        plt.imshow(self.image.astype("uint8"), cmap=cmap)
        plt.show()

    def save(self, path):
        cv2.imwrite(path, self.image)


@dataclass
class Pixel:
    viewport: Viewport
    x: int
    y: int

    @property
    def color(self):
        return self.viewport.image[self.y, self.x]

    @color.setter
    def color(self, value):
        # print(
        #     f"{self.y=}, {self.x=}, {value=}, {self.viewport.image[self.y, self.x]:.2f}"
        # )
        self.viewport.image[self.y, self.x] = value

    def __complex__(self):
        return complex(self.y, -self.x) * self.viewport.scale + self.viewport.offset
