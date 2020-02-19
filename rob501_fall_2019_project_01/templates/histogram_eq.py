import numpy as np

def histogram_eq(I):
        """
        Histogram equalization for greyscale image.

        Perform histogram equalization on the 8-bit greyscale intensity image I
        to produce a contrast-enhanced image J. Full details of the algorithm are
        provided in the Szeliski text.

        Parameters:
        -----------
        I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).

        Returns:
        --------
        J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
        """
        #--- FILL ME IN ---

        # Verify I is grayscale.
        if I.dtype != np.uint8:
            raise ValueError('Incorrect image format!')
        else:
            # Histogram
            H, bins = np.histogram(I.flatten(), bins = 255, range = (0,255), normed = True)
            # CDF
            C = H.cumsum()
            # Normalize 
            C = 255 * C / C[-1]
            # Linear interpolation of CDF to find new pixel values
            J = np.interp(I.flatten(), bins[:-1], C)
            
            J = J.reshape(I.shape)
        #------------------

        return J
