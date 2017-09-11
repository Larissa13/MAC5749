import numpy as np

from skimage import measure

def extract_contours(img):
    contours = measure.find_contours(img, 0)
    contours_lens = np.array([len(c) for c in contours])
    sort_order = (-contours_lens).argsort()
    return([[np.array([j, contours[i][j][0], contours[i][j][1]], dtype = int) for j in range(len(contours[i]))] for i in sort_order])
    
def contour_image(img, obj = 0):
    out = np.zeros(img.shape)
    contour = extract_contours(img)[obj].astype(int)
    for pixel in contour:
        out[pixel[0], pixel[1]] = np.uint8(1)
    return(out)