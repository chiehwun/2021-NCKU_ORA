import pulp
import numpy as np
from matplotlib import pyplot as plt
from pulp.apis.glpk_api import GLPK_CMD


if __name__ == '__main__':
    for i in range(0, 3):
        # Initialize Class
        lp = pulp.LpProblem("Maximize_Profits" if i ==
                            0 else "Minimize_Pollution", pulp.LpMaximize)

        # Define Decicison Variables
        x1 = pulp.LpVariable(name="Production_Rate_G1",
                             lowBound=0, cat='Continuous')
        x2 = pulp.LpVariable(name="Production_Rate_G2",
                             lowBound=0, cat='Continuous')

        # Define Objective Function
        if i == 0:
            lp += 3*x1 + 5*x2
        if i == 1:
            lp += -2*x1 - 4*x2
        if i == 2:
            lp += 3*x1 + 5*x2
        print("Objective Function:\n    ", lp.objective)

        # Define Constraints
        lp += x1 <= 4
        lp += x2 <= 6
        lp += 3*x1 + 2*x2 <= 18
        if i == 2:
            lp += -2*x1 - 4*x2 >= -28
        print("\nConstraints:")
        for name, constraint in lp.constraints.items():
            print(name+':', constraint)

        # Solve Model
        try:
            s = lp.solve(GLPK_CMD(msg=False))
            sol_dict = {1: 'Optimal', 2: 'Not Solved',
                        3: 'Infeasible', 4: 'Unbounded', 5: 'Undefined'}
            if 1 <= s <= 5:
                print("Solver status:", sol_dict[s])
        except Exception as e:
            print("\n\nmodel.solve() has raised an ERROR:", e)

        # Print Solution
        print('='*10, f'Result {i}', '='*10)
        for var in lp.variables():
            print(f'{str(var):>17} =', pulp.value(var))
        print(' '*6, 'Total Profits =', pulp.value(lp.objective))
