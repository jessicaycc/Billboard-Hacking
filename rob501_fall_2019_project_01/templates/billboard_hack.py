# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def billboard_hack():
        """
        Hack and replace the billboard!

        Parameters:
        ----------- 

        Returns:
        --------
        Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
        """
        # Bounding box in Y & D Square image.
        bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

        # Point correspondences.
        Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
        Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])
        Iyd = imread('../billboard/yonge_dundas_square.jpg')
        Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

        Ihack = np.asarray(Iyd)
        Ist = np.asarray(Ist)

        #--- FILL ME IN ---

        # Let's do the histogram equalization first.
        Ist_hist = histogram_eq(Ist)

        # Compute the perspective homography we need...
        H, A = dlt_homography(Iyd_pts, Ist_pts)

        # Main 'for' loop to do the warp and insertion - 
        # this could be vectorized to be faster if needed!
        # You may wish to make use of the contains_points() method
        # available in the matplotlib.path.Path class!

        path = Path(Iyd_pts.T)
        
        for i in range (min(bbox[0]), max(bbox[0])+1):
                for j in range (min(bbox[1]), max(bbox[1])+1):
                        if path.contains_points([[i, j]]):
                                # Use homograph matrix found above to find the corresponding points 
                                x = np.array ([[i],[j], [1]])
                                Ist_pts_homo = H @ x
                                Ist_pts_homo /= Ist_pts_homo[-1]
                                # Compute new pixal value
                                Ihack[j][i] = bilinear_interp(Ist_hist, Ist_pts_homo[:-1, :]) 
        #------------------

        # plt.imshow(Ihack)
        # plt.show()
        # imwrite(Ihack, 'billboard_hacked.png')

        return Ihack

