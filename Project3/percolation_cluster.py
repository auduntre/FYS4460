from scipy.ndimage.measurements import label
from skimage.measure import regionprops
from skimage.color import label2rgb	

import matplotlib.pyplot as plt
import numpy as np


class Percolation_Cluster:
    def __init__(self, p, L):
	self.p = p
        self.L = L
        self.r = np.random.rand(L, L)
        self.z = self.r < p
        self.label_array, self.number = label(self.z)

    def __call__(self, p=None, L=None):
        if p is not None and L is not None:
            __init__(p, L)
        return self.z

    def visualize(self):
        plot = plt.imshow(self.z)
        plt.show()

    def get_labels(self):
        return self.label_array, self.number

    def visualize_label(self):
        label_img = label2rgb(self.label_array, bg_label=0, bg_color=[0.3, 0.3, 0.3])
        plt.imshow(label_img)
        plt.show()
        return label_img

    def region_area(self):
        regions_info = regionprops(self.label_array)
        regions_area = [regions_info[i]['area'] for i in range(len(regions_info))]
        return regions_area


def visualize_percolation_cluster(p, L):
	pc = Percolation_Cluster(p, L)
	pc.visualize()
