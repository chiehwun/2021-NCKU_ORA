import pulp
import numpy as np
import matplotlib.pyplot as plt
from pulp.apis.glpk_api import GLPK_CMD
from pulp.pulp import lpSum, LpVariable, LpProblem, value
from itertools import combinations
from matplotlib import pyplot as plt
import operator as op
from functools import reduce


def ncr(n, r):  # Use math.comb() instead in Python 3.8
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2


if __name__ == '__main__':
    # A = combinations(range(2), 2)
    # for i, j in A:
    #     print(f'i = {i}, j = {j}')
    # exit()

    # Parameters
    W = np.array([[5, 3, 0, 0], [0, 1, 8, 4]])
    V = np.array([[0, 6], [6, 0]])
    a = np.array([0, 4, 6, 10])
    b = np.array([2, 0, 8, 4])

    # Initialize Class
    lp = LpProblem("Minimize_Costs", pulp.LpMinimize)

    # Define Decicison Variables
    x3 = LpVariable(name="sugar_beet_area", lowBound=0)
    var_keys = np.arange(W.shape[0])
    X = LpVariable.dict("new_location_x", var_keys, lowBound=0)
    Y = LpVariable.dict("new_location_y", var_keys, lowBound=0)
    aux_v_keys = np.arange(ncr(W.shape[0], 2))
    P = LpVariable.dict("p", aux_v_keys, lowBound=0)
    Q = LpVariable.dict("q", aux_v_keys, lowBound=0)
    C = LpVariable.dict("c", aux_v_keys, lowBound=0)
    D = LpVariable.dict("d", aux_v_keys, lowBound=0)
    aux_w_keys = np.arange(W.size)
    R = LpVariable.dict("r", aux_w_keys, lowBound=0)
    S = LpVariable.dict("s", aux_w_keys, lowBound=0)
    E = LpVariable.dict("e", aux_w_keys, lowBound=0)
    F = LpVariable.dict("f", aux_w_keys, lowBound=0)

    # Define Objective Function
    lp += lpSum(V[j, k] * (P[_i] + Q[_i])
                for _i, (j, k) in enumerate(combinations(range(W.shape[0]), 2))) + \
        lpSum(lpSum(W[j, i] * (R[j * W.shape[1] + i] + S[j * W.shape[1] + i])
                    for i in range(W.shape[1])) for j in range(W.shape[0])) + \
        lpSum(V[j, k] * (C[_i] + D[_i])
              for _i, (j, k) in enumerate(combinations(range(W.shape[0]), 2))) + \
        lpSum(lpSum(W[j, i] * (E[j * W.shape[1] + i] + F[j * W.shape[1] + i])
                    for i in range(W.shape[1])) for j in range(W.shape[0]))
    print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    for _i, (j, k) in enumerate(combinations(range(W.shape[0]), 2)):
        lp += X[j] - Q[_i] + P[_i] == X[k]
        lp += Y[j] - C[_i] + D[_i] == Y[k]

    for j in range(W.shape[0]):
        for i in range(W.shape[1]):
            lp += X[j] - R[j * W.shape[1] + i] + S[j * W.shape[1] + i] == a[i]
            lp += Y[j] - E[j * W.shape[1] + i] + F[j * W.shape[1] + i] == b[i]

    # print("\nConstraints:")
    # for name, constraint in lp.constraints.items():
    #     print(name+':', constraint)

    # Solve Model
    try:
        s = lp.solve(GLPK_CMD(msg=False))
        # print("\nSolver status:", s)
        REP_sol = value(lp.objective)
    except Exception as e:
        print("\n\nmodel.solve() has raised an ERROR:", e)

    # Print Solution
    print("\n========== Result ==========")
    # for var in lp.variables():
    #     print(f"{str(var):>17} =", value(var))

    for i in var_keys:
        print(f'x_{i} = {value(X[i])}')
        print(f'y_{i} = {value(Y[i])}')
    print("Total Costs =", value(lp.objective))

    X_coord = np.array([value(X[i]) for i in var_keys])
    Y_coord = np.array([value(Y[i]) for i in var_keys])
    plt.figure(figsize=(5, 5))
    plt.scatter(X_coord, Y_coord)
    plt.scatter(a, b)
    plt.title('Graphic Result')
    plt.legend(['New Facilities', 'Existed Facilities'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.savefig('A3P1_Graphic Result.png')
    plt.show()
