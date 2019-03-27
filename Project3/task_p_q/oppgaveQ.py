from scipy.ndimage import measurements
from scipy.stats import linregress
from walk import walk
from pylab import *

Ler = array([i for i in range(50,301,50)])
simulations = 100
p_c = 0.59275
per = array([p_c+0.01*i for i in range(20)])
Dscer= zeros(len(per))
Her= zeros(len(per))

mass_array = zeros((len(per),len(Ler)))
for j, p in enumerate(per):
    for i, L in enumerate(Ler):
        mass_zzz = 0 
        for n in range(simulations):
            perc = []
            ncount=0
            while (len(perc)==0):
                ncount = ncount + 1
                if (ncount >100):
                print "Couldn't make percolation cluster..."
                break
                
                z=rand(L,L)<p
                lw,num = measurements.label(z)
                perc_x = intersect1d(lw[0,:],lw[-1,:])
                perc = perc_x[where(perc_x > 0)]
             #   print ncount

            if len(perc) > 0:
                labelList = arange(num + 1)
                area = measurements.sum(z, lw, index=labelList)
                areaImg = area[lw]
                maxArea = area.max()
                zz = (lw == perc[0])
                l,r = walk(zz)
                zzz = l*r
                mass_zzz += count_nonzero(zzz)
                
        print float(mass_zzz)/simulations
        mass_array[j, i]= float(mass_zzz)/simulations

    print mass_array 
    log_Ler= log(Ler)
    log_mass_array= log(mass_array[j])
    Dsc, H , _,_,_= linregress(log_Ler,log_mass_array)
    Dscer[j] = Dsc
    Her[j] = exp(H)
    
print Dscer
    
figure()
plot(Ler,mass_array[0], "o", linewidth= 3, markersize= 10)
plot(Ler, Her[0]*Ler**Dscer[0], label="linear reg of L^Dsc, p={}".format(p_c))

xlabel("L")
ylabel("Mass of singly connected bonds")
legend()
figure()

for L in Ler:
    plot(per-p_c,Her*L**(Dscer-2), label= "L={}".format(L))

xlabel("p-pc")
ylabel("Psc")
legend()
show()
