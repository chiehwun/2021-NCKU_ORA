###### Problem 1 ######
import pulp
import numpy as np
from pulp.apis.glpk_api import GLPK_CMD

if __name__ == '__main__':
    # Stochastic LP var
    yields = {"high": np.array([3, 3.6, 24]), "avg": np.array(
        [2.5, 3, 20]), "low": np.array([2, 2.4, 16])}

    # Scenarios
    ev = (yields["high"] + yields["avg"] +
          yields["low"]) / 3  # equal probability
    print("Expected yields:", ev)

    # Initialize Class
    lp = pulp.LpProblem("Maximize_Profits", pulp.LpMaximize)

    # Define Decicison Variables
    x1 = pulp.LpVariable(name="wheat_area", lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable(name="corn_area", lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable(name="sugar_beet_area", lowBound=0, cat='Continuous')
    y1 = pulp.LpVariable(name="wheat_buy", lowBound=0, cat='Continuous')
    y2 = pulp.LpVariable(name="corn_buy", lowBound=0, cat='Continuous')
    z1 = pulp.LpVariable(name="wheat_sell", lowBound=0, cat='Continuous')
    z2 = pulp.LpVariable(name="corn_sell", lowBound=0, cat='Continuous')
    z3 = pulp.LpVariable(name="sugar_beet_sellH", lowBound=0, cat='Continuous')
    z4 = pulp.LpVariable(name="sugar_beet_sellL", lowBound=0, cat='Continuous')

    # Define Objective Function
    lp += -150*x1 - 230*x2 - 260*x3 - 238*y1 - \
        210*y2 + 170*z1 + 150*z2 + 36*z3 + 10*z4
    print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    lp += x1 + x2 + x3 <= 500
    lp += ev[0]*x1 + y1 - z1 >= 200
    lp += ev[1]*x2 + y2 - z2 >= 240
    lp += z3 + z4 <= ev[2]*x3
    lp += z3 <= 6000

    print("\nConstraints:")
    for name, constraint in lp.constraints.items():
        print(name+':', constraint)

    # Solve Model
    try:
        s = lp.solve(GLPK_CMD(msg=False))
        print("\nSolver status:", s)
    except Exception as e:
        print("\n\nmodel.solve() has raised an ERROR:", e)

    # Print Solution
    print("\n========== Result (Expected Value) ==========")
    for var in lp.variables():
        print(f"{str(var):>17} =", pulp.value(var))
    print(' '*6, "Total Profits =", pulp.value(lp.objective))

    # print(lp1)
