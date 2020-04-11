#!
#! mosaic module.
#!
import cv2

#! Mosaic function. 
def mosaic(img, rect, size):
    #! Get the area to mosaic.
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]

    #! Once reduced and expanded.
    i_small = cv2.resize(i_rect, (size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)

    #! Overlay mosaic image on image.
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2
