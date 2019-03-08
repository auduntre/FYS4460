from scipy.ndimage.measurements import label
from skimage.measure import regionprops
from skimage.color import label2rgb	

import matplotlib.pyplot as plt
import numpy as np


class Percolation_Cluster:
    """ Class for createing and visualize percolation clusters."""

    def __init__(self, p, L):
        """ Creates the percolation matrix z. """
        self.p = p
        self.L = L
        self.r = np.random.rand(L, L)
        self.z = self.r < p
        self.label_array, self.number = label(self.z)

    def __call__(self, p=None, L=None):
        """ Creates and returns the percolation matrix z. """
        if p is not None and L is not None:
            __init__(p, L)
        return self.z

    def visualize(self):
        """ 
        Visualize the percolation matrix consisting of occupied (1) and 
        unoccupied (0) sites. 
        """
        plot = plt.imshow(self.z)
        plt.show()

    def get_labels(self):
        """
        Returns the percolation matrix with labels clusters by number and the 
        number of clusters.
        """
        return self.label_array, self.number

    def visualize_label(self):
        """ Visualizes the labeled clusters. """
        label_img = label2rgb(self.label_array, bg_label=0, bg_color=[0.3, 0.3, 0.3])
        plt.imshow(label_img)
        plt.show()
        return label_img

    def region_area(self):
        """ Calculates and returns the area of all the clusters."""
        regions_info = regionprops(self.label_array)
        region_areas = [regions_info[i]['area'] for i in range(len(regions_info))]
        return regions_areas

    def region_bbox(self):
        """ Calculates and returns the bbox of all the clusters. """
        regions_info = regionprops(self.label_array)
        region_bboxs = [regions_info[i]['bbox'] for i in range(len(regions_info))]
        return region_bboxs

    def big_P(self):
        bboxs = self.region_bbox()
        print(bboxs)


def visualize_percolation_cluster(p, L):
	pc = Percolation_Cluster(p, L)
	pc.visualize()
