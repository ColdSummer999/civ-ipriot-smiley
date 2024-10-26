
from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrow()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [50, 53, 43, 44]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        """
        Draws eyes on a smiley
        """
        eyes = [18, 21, 26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK

    def draw_eyebrow(self):
        """
        Draws eyebrows on a smiley
        """
        eyebrow = [9, 14]
        for pixel in eyebrow:
            self.pixels[pixel] = self.BLANK

    def blink(self):
        pass
