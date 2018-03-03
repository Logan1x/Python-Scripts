import numpy as np
from numba import jit


@jit
def aprox_pi(N):
    points = 2 * np.random.rand(N, 2) - 1
    M = 0

    for k in range(N):
        if points[k, 0]**2 + points[k, 1]**2 < 1.:
            M += 1

    return 4.*M/N


print(aprox_pi(1e8))
