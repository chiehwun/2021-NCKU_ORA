import pulp
import numpy as np
from pulp.apis.glpk_api import GLPK_CMD
import scipy as sp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Sample Average Approximation
    # N = 30  # sample size
    N = 30  # sample size
    M = 15  # batches
    delta = np.random.normal(1, 0.1, N)  # Random Sampling
    avg_yield = [2.5, 3, 20]

    # Test for DEP
    # yields = np.array([[3, 3.6, 24], [2.5, 3, 20], [2, 2.4, 16]])

    # Initialize Class
    lp = pulp.LpProblem("Maximize_Profits", pulp.LpMaximize)

    # Define Decicison Variables
    # 1st stage
    x1 = pulp.LpVariable(name="wheat_area", lowBound=0)
    x2 = pulp.LpVariable(name="corn_area", lowBound=0)
    x3 = pulp.LpVariable(name="sugar_beet_area", lowBound=0)
    # 2nd stage
    var_keys = np.arange(N)
    Y_1 = pulp.LpVariable.dict("wheat_buy", var_keys, lowBound=0)
    Y_2 = pulp.LpVariable.dict("corn_buy", var_keys, lowBound=0)
    Z_1 = pulp.LpVariable.dict("wheat_sell", var_keys, lowBound=0)
    Z_2 = pulp.LpVariable.dict("corn_sell", var_keys, lowBound=0)
    Z_3 = pulp.LpVariable.dict("sugar_beet_sellH", var_keys, lowBound=0)
    Z_4 = pulp.LpVariable.dict("sugar_beet_sellL", var_keys, lowBound=0)

    # Define Objective Function
    coeff_dict = dict(zip(np.arange(6), [-238, -210, 170, 150, 36, 10]))
    rv_dict = dict(zip(np.arange(6), [Y_1, Y_2, Z_1, Z_2, Z_3, Z_4]))
    lp += -150*x1 - 230*x2 - 260*x3 + \
        pulp.lpSum(pulp.lpSum(coeff_dict[j]*rv_dict[j][i]
                              for j in np.arange(6)) for i in var_keys) / N
    # print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    lp += x1 + x2 + x3 <= 500
    for i in var_keys:
        lp += delta[i]*avg_yield[0]*x1 + Y_1[i] - Z_1[i] >= 200
        lp += delta[i]*avg_yield[1]*x2 + Y_2[i] - Z_2[i] >= 240
        lp += Z_3[i] + Z_4[i] <= delta[i]*avg_yield[2]*x3
        lp += Z_3[i] <= 6000

    # print("\nConstraints:")
    # for name, constraint in lp.constraints.items():
    #     print(name+':', constraint)

    # Solve Model
    try:
        s = lp.solve(GLPK_CMD(msg=False))
        # print("\nSolver status:", s)
        REP_sol = pulp.value(lp.objective)
    except Exception as e:
        print("\n\nmodel.solve() has raised an ERROR:", e)

    # Print Solution
    # print("\n========== Result ==========")
    # for var in lp.variables():
    #     print(f"{str(var):>17} =", pulp.value(var))
    # print(' '*6, "Total Profits =", pulp.value(lp.objective))
