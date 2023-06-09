# import dark
from erase import mosaic
from erase import dark


def erase(img, coordinate_list, type='mosaic'):
    for coordinate in coordinate_list:
        if type == 'mosaic':
            img = mosaic.mosaic(img, coordinate)
        elif type == 'dark':
            img = dark.dark(img, coordinate)
    return img
