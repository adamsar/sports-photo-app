"""
Image processing functions and tasks
"""

from cStringIO import StringIO

import urllib2
import Image

PREVIEW_URL = "http://thumb.usatodaysportsimages.com/image/thumb/{}-{}nw/{}.jpg"

def half_of(a, b):
    return (a - b) / 2

def get_ratio(size):
    return size[0] / float(size[1])

def resize_and_crop(img, size=[], crop_type='middle'):
    i_width = size[0]
    i_height = size[1]
    c_width = img.size[0]
    c_height = img.size[1]
    
    current_ratio = get_ratio(img.size)
    ideal_ratio = get_ratio(size)

    def horizontal_crop():
        modified_image = img.resize(
            (i_width, i_width * c_height / c_width),
            Image.ANTIALIAS)
        
        box = {
            'top': lambda: (0, 0, i_width, c_height),
            'middle': lambda: (0,
                               half_of(c_height, i_height),
                               c_width,
                               half_of(c_height, i_width)),
            'bottom': lambda: (0,
                               c_height - i_height,
                               c_width,
                               c_height)
        }
        return modified_image.crop(box.get(crop_type, box['middle'])())
        
    def vertical_crop():
        modified_image = img.resize(
            (c_height * i_width / c_height, c_height),
            Image.ANTIALIAS)

        box = {
            'top': (0, 0, i_width, c_height),
            'middle': (half_of(c_width, i_width),
                       0,
                       (c_width + i_width) / 2,
                       c_height),
            'bottom': (c_width - i_width,
                       0,
                       c_width,
                       i_height)
            }
        return modified_image.crop(box.get(crop_type, box['middle'])())

    if ideal_ratio > current_ratio:
        return horizontal_crop()
    elif ideal_ratio < current_ratio:
        return vertical_crop()
    else:
        return img.resize(size, Image.ANTIALIAS)

def read_image(url):
    """Reads an image into PIL from a specified URL"""
    f = urllib2.urlopen(url)
    img = StringIO(f.read())
    return Image.open(img)
