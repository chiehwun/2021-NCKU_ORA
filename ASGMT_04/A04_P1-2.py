import pulp
import numpy as np
from matplotlib import markers, pyplot as plt
from pulp.apis.glpk_api import GLPK_CMD


def feasible_area(nx, ny):
    x = np.linspace(0, 4, nx)
    y = np.linspace(0, 6, ny)
    xv, yv = np.meshgrid(x, y)
    xv = xv.flatten()
    yv = yv.flatten()
    ind = []
    for i, (_x, _y) in enumerate(zip(xv, yv)):
        if 3*_x + 2*_y > 18:
            ind.append(i)
    xv = np.delete(xv, ind)
    yv = np.delete(yv, ind)
    return xv, yv


if __name__ == '__main__':
    # Initialize Class
    lp1 = pulp.LpProblem("Maximize_Profits", pulp.LpMaximize)

    # Define Decicison Variables
    x1 = pulp.LpVariable(name="Production_Rate_G1",
                         lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable(name="Production_Rate_G2",
                         lowBound=0, cat='Continuous')

    # Define Objective Function
    lp1 += 4*x1 + 6*x2
    print("Objective Function:\n    ", lp1.objective)

    # Define Constraints
    lp1 += x1 <= 4
    lp1 += x2 <= 6
    lp1 += 3*x1 + 2*x2 <= 18

    print("\nConstraints:")
    for name, constraint in lp1.constraints.items():
        print(name+':', constraint)

    # Solve Model
    try:
        s = lp1.solve(GLPK_CMD(msg=False))
        sol_dict = {1: 'Optimal', 2: 'Not Solved',
                    3: 'Infeasible', 4: 'Unbounded', 5: 'Undefined'}
        if 1 <= s <= 5:
            print("Solver status:", sol_dict[s])
    except Exception as e:
        print("\n\nmodel.solve() has raised an ERROR:", e)

    # Print Solution
    print('='*10, 'Result', '='*10)
    for var in lp1.variables():
        print(f'{str(var):>17} =', pulp.value(var))
    print(' '*6, 'Total Profits =', pulp.value(lp1.objective))

    # Graphical Methods
    # repeat the first point to create a 'closed loop'
    polygen = np.array([[0, 0], [4, 0], [4, 3], [2, 6], [0, 6], [0, 0]])
    xp, yp = zip(*polygen)
    xx, yy = feasible_area(200, 200)  # Feasilbe Area points
    fig, ax1 = plt.subplots(figsize=(8, 8), tight_layout=True)
    ax1.set_title('Decision Variable Space', fontsize=24, fontweight='bold')
    obj_fx = [1.75, 3]
    obj_fy = [(22 - 2*_x)/3 for _x in obj_fx]
    ax1.plot(xx, yy, '.', c="gray", markersize=1)   # feasible area
    ax1.plot(xp, yp, '.-', markersize=17)

    ax1.plot(obj_fx, obj_fy, '--', c='tab:red')  # objective function
    ax1.annotate("", xy=(2.8 + 0.2, (22 - 2*2.8)/3 + 0.3), xytext=(2.8, (22 - 2*2.8)/3),
                 arrowprops=dict(arrowstyle="->", color='tab:red'))
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    # Constraints
    # test = dict(fontsize=20, c='tab:blue')
    ax1.text(-0.5, 3, '$x_1 = 0$', ha='center',
             va='center', fontsize=20, c='tab:blue')
    ax1.text(4.1, 1.5, '$x_1 = 4$', ha='left',
             va='center', fontsize=20, c='tab:blue')
    ax1.text(2, -0.2, '$x_2 = 0$', ha='center',
             va='center', fontsize=20, c='tab:blue')
    ax1.text(1, 6.2, '$x_2 = 6$', ha='center',
             va='center', fontsize=20, c='tab:blue')
    ax1.text(3.1, 4.5, '$3x_1 + 2x_2 = 18$',
             ha='left', va='center', fontsize=20, c='tab:blue')
    ax1.text(3.1, 5.6, '$Z(x_1, x_2)$',
             ha='left', va='center', fontsize=20, c='tab:red')
    # Points label
    ax1.text(-0.1, 0, '$A(0,0)$', ha='right', va='center', fontsize=20)
    ax1.text(4.1, 0, '$B(4,0)$', ha='left', va='center', fontsize=20)
    ax1.text(4.1, 3, '$C(4,3)$', ha='left', va='center', fontsize=20)
    ax1.text(2.2, 6, '$D(2,6)$', ha='left', va='center', fontsize=20)
    ax1.text(-0.1, 6, '$E(0,6)$', ha='right', va='center', fontsize=20)
    # axis, aspect
    ax1.set_xlabel('$x_1$', fontsize=20)
    ax1.set_ylabel('$x_2$', fontsize=20)
    ax1.set_xticks(range(0, 5))
    dd = 0.6
    ax1.set_xlim([-2+dd, 6-dd])
    ax1.set_ylim([-1+dd, 7-dd])
    ax1.set_aspect('equal', adjustable='box')  # avoid text out of range
    plt.savefig('ASGMT_04/P1-2_Weighting Method')
    plt.show()
