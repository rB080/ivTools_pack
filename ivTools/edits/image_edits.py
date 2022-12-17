from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
import numpy as np


def pilToNumpy(img):
    return np.array(img)


def NumpyToPil(img):
    return Image.fromarray(img)


def attach(im1, im2, orientation="horizontal"):
    assert im1.shape[2] == im2.shape[2], "Channel number mismatch error."

    im1, im2 = NumpyToPil(im1), NumpyToPil(im2)

    assert orientation in [
        "horizontal", "vertical"], "Unrecognized orientation for concatenation."

    if orientation == "horizontal":
        assert im1.size[1] == im2.size[1], "Height mismatch error."
    else:
        assert im1.size[0] == im2.size[0], "Width mismatch error."

    # Dimensioning
    dims = list(im1.size)
    if orientation == "horizontal":
        dims[0] += im2.size[0]
    else:
        dims[1] += im2.size[1]

    # Attachment
    blank = Image.new('RGB', (dims[0], dims[1]))
    blank.paste(im1, (0, 0))
    if orientation == "horizontal":
        blank.paste(im2, (im1.width, 0))
    else:
        blank.paste(im2, (0, im1.height))

    blank = pilToNumpy(blank)
    return blank


def annotate(img, text, position=(0, 0), color="black", font_size=1, font="fonts/arial.ttf"):
    img = NumpyToPil(img)
    console = ImageDraw.Draw(img)
    if font == "default":
        fn = ImageFont.load_default()
    else:
        fn = ImageFont.truetype(font, size=font_size)

    console.text(position, text, font=fn, fill=color)

    img = pilToNumpy(img)
    return img
