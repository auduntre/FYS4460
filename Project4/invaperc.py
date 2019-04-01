from pylab import *
from scipy.ndimage import measurements


L = 100 # system size
p = linspace(0,0.7,71)
perc = 0 # flag to signal if other end is reached
nbetween = 1
nstep = 0
nend = len(p)
nstop = 0
z = rand(L,L)  # Random distribution of thresholds 
pcluster = zeros((L,L)) 
while ((nstop==0) and (nstep<nend)): 
	nstep = nstep + 1 
	p0 = p[nstep] 
	zz = z<p0 
	[lw,num] = measurements.label(zz) 
	leftside = lw[:,0] 
	il = argwhere(leftside>0)
	leftnonzero = leftside[il]  
	#print leftside
	uniqueleftside = unique(leftnonzero) 
	#print uniqueleftside
	cluster = isin(lw, uniqueleftside) #ismember(lw,uniqueleftside)
	print cluster
	pcluster = pcluster + cluster.astype(float) 
	#print pcluster
	
	#if (nstep % nbetween==0):
	#	imshow(pcluster)
	#	colorbar()
	#	show()
	
	# Check if it has reached the right hand side
	rightside = lw[:,-1] 
	ir = argwhere(rightside>0) 
	rightnonzero = rightside[ir] 
	span = intersect1d(leftnonzero,rightnonzero)
	if len(span)>0: 
		nstop = 1  # spanning end

print p0
im = imshow(pcluster, animated=True, cmap=cm.Set3)
colorbar()
show()
