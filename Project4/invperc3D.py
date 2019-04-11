from scipy.ndimage import measurements
import numpy as np


def std_case():
    L = 100
    MCCs = 1000
    p = np.linspace(0.0, 0.4, 41)
    return p, L, MCCs


def inv_perc_sim(p, L, MCCs):
    pcs = np.zeros(MCCs)
    Ns = np.zeros((len(p), MCCs))

    for mi in range(MCCs):
        perc = 0
        nstep = 1
        nend = len(p)
        z = np.random.rand(L, L, L)   # Random dist of threasholds
        pcluster = np.zeros((L, L, L))

        while nstep < nend:
            p0 = p[nstep]
            zz = z < p0
            [lw, num] = measurements.label(zz)

            # Find clusters connected to "left side"
            leftside = lw[0, :, :]
            il = np.nonzero(leftside)
            leftnonzero = leftside[il]
            unique_leftside = np.unique(leftnonzero)

            # updating invasion
            cluster = np.isin(lw, unique_leftside)
            pcluster = pcluster + cluster.astype(float)
            Ns[nstep - 1, mi] = len(cluster[cluster == True])

            # Find clustes connected to "right side"
            rightside = lw[-1, :, :]
            ir = np.nonzero(rightside)
            rightnonzero = rightside[ir]

            # Check if invasion percolation
            span = np.intersect1d(leftnonzero, rightnonzero)

            if len(span) > 0:
                pcs[mi] = p0
                break
            
            nstep += 1
    return Ns, pcs


def inv_perc_sim_corner(p, L, MCCs):
    pcs = np.zeros(MCCs)
    Ns = np.zeros((len(p), MCCs))

    for mi in range(MCCs):
        perc = 0
        nstep = 1
        nend = len(p)
        z = np.random.rand(L, L, L)   # Random dist of threasholds
        pcluster = np.zeros((L, L, L))

        while nstep < nend:
            p0 = p[nstep]
            zz = z < p0
            [lw, num] = measurements.label(zz)

            # Find clusters connected to "left side"
            leftside = lw[0, 0, :]
            il = np.nonzero(leftside)
            leftnonzero = leftside[il]
            unique_leftside = np.unique(leftnonzero)

            # updating invasion
            cluster = np.isin(lw, unique_leftside)
            pcluster = pcluster + cluster.astype(float)
            Ns[nstep - 1, mi] = len(cluster[cluster == True])

            # Find clustes connected to "right side"
            rightside = lw[-1, -1, :]
            ir = np.nonzero(rightside)
            rightnonzero = rightside[ir]

            # Check if invasion percolation
            span = np.intersect1d(leftnonzero, rightnonzero)

            if len(span) > 0:
                pcs[mi] = p0
                break
            
            nstep += 1
    return Ns, pcs


def main(plot_it=False, save_it=False):
    p, L, M = std_case()
    Ns, pcs = inv_perc_sim(p, L, M)
    print(f"mean(Ns[1, :]) = {Ns[1, :].mean()}")
    print(f"mean(p_c) = {pcs.mean():.8f}")

    if plot_it:
        import matplotlib.pyplot as plt
        
        start = 0.05
        end = 0.30
        N = int((end - start) / start)
    
        values = np.linspace(start, end, N + 1)
        pis = np.argwhere(np.in1d(p, values)).flatten()

        for pi in pis:
            p_hist, n_hist = np.histogram(Ns[pi, :], density=True)
            
            plt.hist(Ns[pi, :], density=True)
            plt.plot(0.5*(n_hist[1:] + n_hist[:-1]), p_hist, 'r-')

            plt.title(f"Prob_pres = {p[pi]:.2f}")
            plt.ylabel("Probability for number of sites invaded")
            plt.xlabel("Number of sites invaded")
            plt.show()

    if save_it:
        np.save("results/Ns_serial.npy", Ns)


if __name__ == "__main__":
    main(plot_it=False, save_it=False)
