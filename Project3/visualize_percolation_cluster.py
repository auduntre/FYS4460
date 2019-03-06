from scipy.ndimage.measurements import label
from skimage.color import label2rgb	

import matplotlib.pyplot as plt
import numpy as np

class Percolation_Cluster:
	def __init__(self, p, L):
		self.p = p
		self.L = L
		self.r = np.random.rand(L, L)
		self.z = self.r < p

	def visualize(self):
		plot = plt.imshow(self.z)
		plt.show()

	def get_labels(self	):
		label_array, number = label(self.z)
		return label_array, number

	def visualize_label(self):
		label_array, number = self.get_labels()
		label_img = label2rgb(label_array, bg_label=0, bg_color=[1, 1, 1])
		
		plt.imshow(label_img)
		plt.show()
		return label_img


def visualize_percolation_cluster(p, L):
	pc = Percolation_Cluster(p, L)
	pc.visualize()