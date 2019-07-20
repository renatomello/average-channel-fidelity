#%%
from qutip import * 
from math import sqrt
import numpy as np 
#import matplotlib.pyplot as plt
#import matplotlib as mpl

#%%
N = 10
alpha = (1+1.j) / sqrt(2)
identity_1_mode = qeye(N)

a_1_mode = destroy(N)
q_1_mode = (a_1_mode + a_1_mode.dag()) / 2
p_1_mode = (a_1_mode - a_1_mode.dag()) / 2.j

q_1, p_1 = tensor(q_1_mode, identity_1_mode), tensor(p_1_mode, identity_1_mode)
q_2, p_2 = tensor(identity_1_mode, q_1_mode), tensor(identity_1_mode, p_1_mode)
base = [q_1, p_1, q_2, p_2]

vacuum_1_mode = basis(N,0)
vacuum_2_mode = tensor(vacuum_1_mode, vacuum_1_mode)
displacement_1_mode = displace(N, alpha = alpha)
displacement_2_mode = tensor(displacement_1_mode, displacement_1_mode)
#%%
state = displacement_2_mode * vacuum_2_mode
rho = ket2dm(state)
V = covariance_matrix(basis = base, rho = rho)
V
#%%
