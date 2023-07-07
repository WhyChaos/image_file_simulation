
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import random
import numpy as np
import math
from effects.scan_effect import ScanEffect
from effects.photo_effect import PhotoEffect
from effects.photo_screen_effect import PhotoScreenEffect
from effects.screen_effect import ScreenEffect


class Effect:
    def __init__(self, type='scan'):
        if type == 'scan':
            self.effect = ScanEffect()
        elif type == 'photo':
            self.effect = PhotoEffect()
        elif type == 'photo_screen':
            self.effect = PhotoScreenEffect()
        elif type == 'screen':
            self.effect = ScreenEffect()

    def main(self, image):
        return self.effect.main(image)
