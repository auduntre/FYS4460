from invperc3D import std_case, inv_perc_sim, inv_perc_sim_corner
from mpi4py import MPI
import numpy as np


def main_mpi(plot_it=False, save_it=False, ip_sim_type=inv_perc_sim):
    comm = MPI.COMM_WORLD
    mpi_rank = comm.Get_rank()
    mpi_size = comm.Get_size()
    master = 0
    
    p, L, M = std_case()
    M_rank = M // mpi_size
    
    if mpi_rank == master:
        M_rank += M % mpi_size
    
    Ns, pcs = ip_sim_type(p, L, M_rank)
    pcs_sum = None
    Ns_total = None
    recvline = None

    if mpi_rank == master:
        pcs_sum = np.empty(pcs.shape)
        Ns_total = np.empty([len(p), M])
        recvline = np.empty(M)

    comm.Reduce(pcs, pcs_sum, op=MPI.SUM, root=master)
    Ms = np.array(comm.gather(M_rank, root=master))

    for i in range(len(p)):
        comm.Gatherv(Ns[i, :], (recvline, Ms), root=master)
        
        if mpi_rank == master:
            Ns_total[i, :] = recvline

    if mpi_rank == master:
        print(f"mean(Ns[1, :]) = {Ns_total[1, :].mean()}")
        pcs_avg = np.sum(pcs_sum) / M
        print(f"mean(p_c) = {pcs_avg:.8f}")

        if plot_it:
            import matplotlib.pyplot as plt

            type_sim = ""
            if ip_sim_type is inv_perc_sim_corner:
                type_sim = "corner"

            start = 0.05
            end = 0.30
            N = int((end - start) / start)
        
            values = np.linspace(start, end, N + 1)
            pis = np.argwhere(np.in1d(p, values)).flatten()

            for pi in pis:
                p_hist, n_hist = np.histogram(Ns_total[pi, :], density=True)
                
                plt.hist(Ns_total[pi, :], density=True)
                plt.plot(0.5*(n_hist[1:] + n_hist[:-1]), p_hist, 'r-')

                plt.title(f"Prob_pres = {p[pi]:.2f}, L = {L}, MCCs = {M}")
                plt.ylabel("Probability for number of sites invaded")
                plt.xlabel("Number of sites invaded")
                plt.savefig(f"results/dist{type_sim}_{p[pi]:.2f}.png")
                plt.show()

        if save_it:
            np.save("results/Ns_parallel.npy", Ns_total)


if __name__ == "__main__":
    main_mpi(plot_it=True, save_it=False, ip_sim_type=inv_perc_sim_corner)
