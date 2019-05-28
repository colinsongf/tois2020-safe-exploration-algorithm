import numba
import numpy as np
from experiments.classification import dataset
from experiments.classification.util import reward


@numba.njit(nogil=True)
def evaluate(test_data, policy):
    cum_r_policy = 0.0
    cum_r_best = 0.0
    for i in range(test_data.n):
        x, y = test_data.get(i)
        a_policy = policy.draw(x)
        a_best = policy.max(x)
        r_policy = reward(x, y, a_policy)
        r_best = reward(x, y, a_best)
        cum_r_policy += r_policy
        cum_r_best += r_best
    return cum_r_policy / test_data.n, cum_r_best / test_data.n

