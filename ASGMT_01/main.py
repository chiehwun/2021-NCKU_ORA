###### Problem 1 ######
import pulp
from pulp.apis.glpk_api import GLPK_CMD

if __name__ == '__main__':
    # Initialize Class
    lp = pulp.LpProblem("Minimize_Foods_Costs", pulp.LpMinimize)

    # Define Decicison Variables
    B = pulp.LpVariable(name="bread", lowBound=0, cat='Integer')
    P = pulp.LpVariable(name="peanut_butter", lowBound=0, cat='Integer')
    S = pulp.LpVariable(name="strawberry_jelly", lowBound=0, cat='Integer')
    G = pulp.LpVariable(name="graham_cracker", lowBound=0, cat='Integer')
    M = pulp.LpVariable(name="milk", lowBound=0, cat='Integer')
    J = pulp.LpVariable(name="juice", lowBound=0, cat='Integer')

    # Define Objective Function
    lp += 5*B + 4*P + 7*S + 8*G + 15*M + 35*J
    print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    lp += 70*B + 100*P + 50*S + 60*G + 150*M + 100*J >= 400
    lp += 70*B + 100*P + 50*S + 60*G + 150*M + 100*J <= 600
    lp += 10*B + 75*P + 20*G + 70*M <= 0.3 * \
        (70*B + 100*P + 50*S + 60*G + 150*M + 100*J)
    lp += 3*S + 2*M + 120*J >= 60
    lp += 3*B + 4*P + G + 8*M + J >= 12
    lp += B == 2
    lp += P >= 2*S
    lp += M + J >= 1
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
    print("\n========== Result ==========")
    for var in lp.variables():
        print(f"{str(var):>17} =", pulp.value(var))
    print(' '*6, "Total Cost =", pulp.value(lp.objective))

    # print(lp1)
