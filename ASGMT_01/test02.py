import pulp

from pulp.apis.coin_api import PULP_CBC_CMD
from pulp.apis.glpk_api import GLPK_CMD

# Initialize Class
model = pulp.LpProblem("Maximize_Bakery_Profits", pulp.LpMaximize)

# Define Decicison Variables
A = pulp.LpVariable(name="A", lowBound=0, cat='Integer')
B = pulp.LpVariable(name="C", lowBound=0, cat='Integer')

# Define Objective Function
model += 20 * A + 40 * B
print(model.objective)

# Define Constraints
model += 0.5 * A + 1 * B <= 30
model += 1 * A + 2.5 * B <= 60
model += 1 * A + 2 * B <= 22
print(model.constraints)

# Solve Model
try:
    # model.solve(PULP_CBC_CMD(msg=False))
    # Success
    s = model.solve(GLPK_CMD(msg=False))
    print("Status:", s)
except Exception as e:
    print("\n\nmodel.solve() has raised an ERROR:", e)

# Print Solution
print("Produce {} Cake A".format(A.varValue))
print("Produce {} Cake B".format(B.varValue))
