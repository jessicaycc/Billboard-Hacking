import numpy as np
from numpy.linalg import inv

def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    4 pixels to compute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will 
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    #--- FILL ME IN ---

    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')
    else: 
        x1 = int(pt[0])
        x2 = int(pt[0]) + 1
        y1 = int(pt[1])
        y2 = int(pt[1]) + 1

        # Finding the coefficients by solving the linear system 
        M = np.array([[1, x1, y1, x1 * y1], 
                      [1, x1, y2, x1 * y2], 
                      [1, x2, y1, x2 * y1], 
                      [1, x2, y2, x2 * y2]])

        F = np.array([[I[y1, x1]],
                      [I[y2, x1]],
                      [I[y1, x2]], 
                      [I[y2, x2]]])

        a = inv(M) @ F

        # Plug the found coeffiecients back into the equation to find the new pixal value
        b = a[0] + a[1] * pt[0] + a[2] * pt[1] + a[3] * pt[0]* pt[1]
        b = int(round(b[0]))
    #------------------

    return b
