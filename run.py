import math
import numpy.random as npr
import numpy as np
import itertools


equation_string = "a*x1+b*x2+c*x3+d*x4=n"

coeff = npr.random_integers(1,4,4)
start_gene = npr.random_integers(1,40,(4,4))
N = 40

_test_coeff = (1, 2, 3, 4)
_test_gene = ((1, 28, 15, 3), (14, 9, 2, 4), (13, 5, 7, 3), (23, 8, 16, 19), (9, 13, 5, 2))

def mix_gene(*args):
    i = 0
    X_gene = np.array(args[i])
    Y_gene = np.array(args[i + 1])

    X = X_gene.reshape(2, 2)
    Y = Y_gene.reshape(2, 2)
    child = (np.array(list(itertools.chain(np.hstack((X[0], Y[1])), np.hstack((X[1], Y[0])))))).reshape(2,4)

    print(child)

    return tuple(child[0])


def _check_Solv(cf, xn ):
    a,b,c,d = cf
    x1,x2,x3,x4 = xn
    k = a*x1+b*x2+c*x3+d*x4
    check = abs(k-N)

    return check


print(mix_gene((1, 28, 15, 3), (14, 9, 2, 4)))
print(_check_Solv(_test_coeff, _test_gene[1]))

print()
