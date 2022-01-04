###### Problem 1 ######
import pulp
import numpy as np
from pulp.apis.glpk_api import GLPK_CMD

if __name__ == '__main__':
    # Stochastic LP var
    yields = {"high": np.array([3, 3.6, 24]), "avg": np.array(
        [2.5, 3, 20]), "low": np.array([2, 2.4, 16])}

    # Scenarios
    weather = "high"  # ["high" "avg" "low"]

    # Initialize Class
    lp = pulp.LpProblem("Maximize_Profits", pulp.LpMaximize)

    # Define Decicison Variables
    # 1st stage
    x1 = pulp.LpVariable(name="wheat_area", lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable(name="corn_area", lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable(name="sugar_beet_area", lowBound=0, cat='Continuous')
    # 2nd stage
    y1_1 = pulp.LpVariable(name="wheat_buy_high", lowBound=0, cat='Continuous')
    y2_1 = pulp.LpVariable(name="corn_buy_high", lowBound=0, cat='Continuous')
    z1_1 = pulp.LpVariable(name="wheat_sell_high",
                           lowBound=0, cat='Continuous')
    z2_1 = pulp.LpVariable(name="corn_sell_high", lowBound=0, cat='Continuous')
    z3_1 = pulp.LpVariable(name="sugar_beet_sellH_high",
                           lowBound=0, cat='Continuous')
    z4_1 = pulp.LpVariable(name="sugar_beet_sellL_high",
                           lowBound=0, cat='Continuous')
    y1_2 = pulp.LpVariable(name="wheat_buy_avg", lowBound=0, cat='Continuous')
    y2_2 = pulp.LpVariable(name="corn_buy_avg", lowBound=0, cat='Continuous')
    z1_2 = pulp.LpVariable(name="wheat_sell_avg", lowBound=0, cat='Continuous')
    z2_2 = pulp.LpVariable(name="corn_sell_avg", lowBound=0, cat='Continuous')
    z3_2 = pulp.LpVariable(name="sugar_beet_sellH_avg",
                           lowBound=0, cat='Continuous')
    z4_2 = pulp.LpVariable(name="sugar_beet_sellL_avg",
                           lowBound=0, cat='Continuous')
    y1_3 = pulp.LpVariable(name="wheat_buy_low", lowBound=0, cat='Continuous')
    y2_3 = pulp.LpVariable(name="corn_buy_low", lowBound=0, cat='Continuous')
    z1_3 = pulp.LpVariable(name="wheat_sell_low", lowBound=0, cat='Continuous')
    z2_3 = pulp.LpVariable(name="corn_sell_low", lowBound=0, cat='Continuous')
    z3_3 = pulp.LpVariable(name="sugar_beet_sellH_low",
                           lowBound=0, cat='Continuous')
    z4_3 = pulp.LpVariable(name="sugar_beet_sellL_low",
                           lowBound=0, cat='Continuous')

    # Define Objective Function
    lp += -150*x1 - 230*x2 - 260*x3 + (- 238*y1_1 - 210*y2_1 + 170*z1_1 + 150*z2_1 + 36*z3_1 + 10*z4_1
                                       - 238*y1_2 - 210*y2_2 + 170*z1_2 + 150*z2_2 + 36*z3_2 + 10*z4_2
                                       - 238*y1_3 - 210*y2_3 + 170*z1_3 + 150*z2_3 + 36*z3_3 + 10*z4_3) / 3
    print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    lp += x1 + x2 + x3 <= 500
    lp += yields["high"][0]*x1 + y1_1 - z1_1 >= 200
    lp += yields["avg"][0]*x1 + y1_2 - z1_2 >= 200
    lp += yields["low"][0]*x1 + y1_3 - z1_3 >= 200
    lp += z3_1 + z4_1 <= yields["high"][2]*x3
    lp += z3_2 + z4_2 <= yields["avg"][2]*x3
    lp += z3_3 + z4_3 <= yields["low"][2]*x3
    lp += yields["high"][1]*x2 + y2_1 - z2_1 >= 240
    lp += yields["avg"][1]*x2 + y2_2 - z2_2 >= 240
    lp += yields["low"][1]*x2 + y2_3 - z2_3 >= 240
    lp += z3_1 <= 6000
    lp += z3_2 <= 6000
    lp += z3_3 <= 6000

    print("\nConstraints:")
    for name, constraint in lp.constraints.items():
        print(name+':', constraint)

    # Solve Model
    try:
        s = lp.solve(GLPK_CMD(msg=False))
        print("\nSolver status:", s)
        REP_sol = pulp.value(lp.objective)
    except Exception as e:
        print("\n\nmodel.solve() has raised an ERROR:", e)

    # Print Solution
    print("\n========== Result (RP) ==========")
    for var in lp.variables():
        print(f"{str(var):>17} =", pulp.value(var))
    print(' '*6, "Total Profits =", pulp.value(lp.objective))

    # Calculate EVPI

    # Calculate VSS
    # Uncomment to take into EV solution
    print("Take into EV solution x_ev")
    EV_stg1 = np.array([120, 80, 300])
    lp += x1 == EV_stg1[0]
    lp += x2 == EV_stg1[1]
    lp += x3 == EV_stg1[2]
    lp.solve(GLPK_CMD(msg=False))
    EV_sol = pulp.value(lp.objective)
    print(f"VSS = {REP_sol} - {EV_sol} = {REP_sol - EV_sol}")
