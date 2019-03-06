from scipy.ndimage.measurements import label
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


def visualize_percolation_cluster(p, L):
	pc = Percolation_Cluster(p, L)
	pc.visualize()