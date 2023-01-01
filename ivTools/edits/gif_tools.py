from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
import numpy as np


class GIF_maker():

    def __init__(self) -> None:
        frame_list = []
        frame_rate = 30
        duration = 1000//frame_rate

    def __len__(self):
        return len(self.frame_list)

    def __getitem__(self, index):
        return self.frame_list[index]

    def __add__(self, gif):
        self.frame_list = self.frame_list + gif.frame_list

    def set_frame_rate(self, fps):
        self.frame_rate = fps
        self.duration = 1000//self.frame_rate

    def add_frame(self, img):
        self.frame_list.append(img)

    def save_GIF(self, save_path, slice=None, reset=False):
        frames = self.frame_list
        if slice is not None:
            if len(slice) == 2:
                frames = frames[slice[0]:slice[1]]
            else:
                frames = frames[slice[0]:]
        frame_one = frames[0]
        frame_one.save(save_path, format="GIF", append_images=frames,
                       save_all=True, duration=self.duration, loop=0)

        if reset:
            self.__init__()
