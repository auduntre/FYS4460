from pylab import *
from scipy.ndimage import measurements


L = 50 # system size
p = linspace(0, 0.7, 8)


M = 1000
Ns = zeros((len(p), M))

for mi in range(M):
	z = rand(L,L)  # Random distribution of thresholds 
	pcluster = zeros((L,L))

	perc = 0 # flag to signal if other end is reached
	nbetween = 10
	nstep = 0
	nend = len(p)
	nstop = 0

	plot_invasion = False 

	while ((nstop==0) and (nstep<nend)): 
		nstep = nstep + 1 
		p0 = p[nstep] 
		zz = z < p0 
		[lw,num] = measurements.label(zz) 
		leftside = lw[:,0] 
		il = argwhere(leftside>0)
		leftnonzero = leftside[il]  
		#print leftside
		uniqueleftside = unique(leftnonzero) 
		#print uniqueleftside
		cluster = isin(lw, uniqueleftside) #ismember(lw,uniqueleftside)
		#print cluster 
		pcluster = pcluster + cluster.astype(float)
		Ns[nstep - 1, mi] = len(cluster[cluster == True])
		#print pcluster
		
		if (nstep % nbetween==0) and plot_invasion:
			imshow(pcluster)
			colorbar()
			draw()
			pause(.01)
			show()
			close()
		
		# Check if it has reached the right hand side
		rightside = lw[:,-1] 
		ir = argwhere(rightside>0) 
		rightnonzero = rightside[ir] 
		span = intersect1d(leftnonzero,rightnonzero)
		if len(span)>0: 
			nstop = 1  # spanning end


print p0
if plot_invasion:
	im = imshow(pcluster)
	colorbar()
	draw()
	show()

pis = [1, 2, 3]

for pi in pis:
	hist(Ns[pi, :])
	title(p[pi])
	show()