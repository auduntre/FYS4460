from invperc3D import std_case, inv_perc_sim
from mpi4py import MPI
import numpy as np


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    mpi_rank = comm.Get_rank()
    mpi_size = comm.Get_size()
    master = 0
    

    p, L, M = std_case()
    M_rank = M // mpi_size
    
    if mpi_rank == master:
        M_rank += M % mpi_size
    
    Ns, pcs = inv_perc_sim(p, L, M_rank)
    pcs_all = None

    if mpi_rank == master:
        pcs_all = np.empty([mpi_size, 1])
    

    pcs_all = np.array(comm.gather(pcs.mean(), root=master), dtype=np.float64)
    M_ranks = np.array(comm.gather(M_rank, root=master), dtype=np.float64)

    if mpi_rank == master:
        pcs_avg = np.sum(pcs_all.T * M_ranks / M)
        print(f"mean(p_c) = {pcs_avg:.8f}")
