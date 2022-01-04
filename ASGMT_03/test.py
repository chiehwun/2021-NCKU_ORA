import pulp
from pulp.apis.glpk_api import GLPK_CMD

# Initialize Class
model = pulp.LpProblem("Maximize_Bakery_Profits", pulp.LpMaximize)

# Define Decicison Variables
A = pulp.LpVariable(name="A", lowBound=0, upBound=50, cat='Integer')

# Define Objective Function
model += A
print(model.objective)

# Define Constraints
model += A <= 100
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
print(f'A = {pulp.value(A)}')
