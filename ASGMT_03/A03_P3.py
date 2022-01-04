import pulp
import numpy as np
import matplotlib.pyplot as plt
from pulp.apis.glpk_api import GLPK_CMD
from pulp.pulp import lpSum, LpVariable, LpProblem, value
from itertools import combinations, permutations
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import operator as op
from functools import reduce


def ncr(n, r):  # Use math.comb() instead in Python 3.8
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2


def pnr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    return numer


class Rects:
    def __init__(self):
        self.p = []
        self.q = []
        self.x_max = 0
        self.y_max = 0
        self.x_min = None
        self.y_min = None

    def add(self, p, q, n=1):
        large = max(p, q)
        little = min(p, q)
        self.p = np.append(self.p, np.full(n, large))
        self.q = np.append(self.q, np.full(n, little))
        self.x_max += large*n
        self.y_max += little*n
        if self.x_min is None:
            self.x_min = little
        else:
            self.x_min = min(little, self.x_min)
        self.y_min = self.x_min

    def num(self):
        return self.p.size

    def show(self):
        print(f'Rectangle Number: {self.num()}')
        print(f'P: {self.p}')
        print(f'Q: {self.q}')
        print(f'x_max: {self.x_max}')
        print(f'y_max: {self.y_max}')
        print(f'x_min: {self.x_min}')
        print(f'y_min: {self.y_min}')


def Cutting_Stock(R, m, same, graph_out=True, title='', show_detail=False):
    # m break points
    # Piecewise Linearization of Logarithm Term
    if same:
        R.y_min = R.x_min
        R.y_max = R.x_max
    a = np.linspace(R.x_min, R.x_max, m)
    b = np.linspace(R.y_min, R.y_max, m)
    log_a = np.log(a)
    log_b = np.log(b)
    sl_a = np.array([(log_a[j+1] - log_a[j])/(a[j+1] - a[j])
                    for j in range(m-1)])
    sl_b = np.array([(log_b[j+1] - log_b[j])/(b[j+1] - b[j])
                    for j in range(m-1)])
    if show_detail is True:
        print(f'\nm: {m}')
        # print(f'    a.shape: {a.shape}')
        # print(f'    b.shape: {b.shape}')
        # print(f'ln(a).shape: {log_a.shape}')
        # print(f'ln(b).shape: {log_b.shape}')
        # print(f' sl_a.shape: {sl_a.shape}')
        # print(f' sl_b.shape: {sl_b.shape}')

    # Initialize Class
    lp = LpProblem("Minimize_Area", pulp.LpMinimize)

    # Define Decicison Variables
    x = LpVariable(name="Envelope_x", lowBound=R.x_min, upBound=R.x_max)
    y = LpVariable(name="Envelope_y", lowBound=R.y_min, upBound=R.y_max)
    rect_keys = np.arange(R.num())
    X_c = LpVariable.dict("x_center", rect_keys, lowBound=0)
    Y_c = LpVariable.dict("y_center", rect_keys, lowBound=0)
    S = LpVariable.dict("s_orientation", rect_keys,
                        lowBound=0, upBound=1, cat='Integer')
    comb2_keys = np.arange(ncr(R.num(), 2))
    U = LpVariable.dict("u", comb2_keys, lowBound=0, upBound=1, cat='Integer')
    V = LpVariable.dict("v", comb2_keys, lowBound=0, upBound=1, cat='Integer')
    # Absolute Auxilary Variables
    abs_aux_keys = np.arange(1, m-1)  # 1, 2, ..., m-2
    tx = LpVariable.dict("tx_abs", abs_aux_keys, lowBound=0,
                         upBound=1, cat='Integer')
    wx = LpVariable.dict("wx_abs", abs_aux_keys, lowBound=0)
    ty = LpVariable.dict("ty_abs", abs_aux_keys, lowBound=0,
                         upBound=1, cat='Integer')
    wy = LpVariable.dict("wy_abs", abs_aux_keys, lowBound=0)

    # Define Objective Function
    lp += log_a[0] + sl_a[0] * (x - a[0]) + \
        lpSum((sl_a[j] - sl_a[j-1]) * (a[j]*tx[j] + x - a[j] - wx[j])
              for j in abs_aux_keys) + \
        log_b[0] + sl_b[0] * (y - b[0]) + \
        lpSum((sl_b[j] - sl_b[j-1]) * (b[j]*ty[j] + y - b[j] - wy[j])
              for j in abs_aux_keys)
    # print("Objective Function:\n    ", lp.objective)

    # Define Constraints
    """ Absolute Value """
    for j in abs_aux_keys:
        # ln(x)
        lp += -a[-1]*tx[j] <= x - a[j]
        lp += x - a[j] <= a[-1]*(1 - tx[j])
        lp += -a[-1]*tx[j] <= wx[j]
        lp += wx[j] <= a[-1]*tx[j]
        lp += a[-1]*(tx[j]-1) + x <= wx[j]
        lp += wx[j] <= a[-1]*(1 - tx[j]) + x
        # ln(y)
        lp += -b[-1]*ty[j] <= x - b[j]
        lp += x - b[j] <= b[-1]*(1 - ty[j])
        lp += -b[-1]*ty[j] <= wy[j]
        lp += wy[j] <= b[-1]*ty[j]
        lp += b[-1]*(ty[j]-1) + x <= wy[j]
        lp += wy[j] <= b[-1]*(1 - ty[j]) + x
        if j > 1:
            lp += tx[j] >= tx[j-1]
            lp += ty[j] >= ty[j-1]
    """ Non-overlapping Conditions """
    for ik, (i, k) in enumerate(combinations(np.arange(R.num()), 2)):
        lp += (X_c[i] - X_c[k]) + (U[ik] + V[ik])*R.x_max >= \
            0.5*(R.p[i]*S[i] + R.q[i]*(1 - S[i]) +
                 R.p[k]*S[k] + R.q[k]*(1 - S[k]))
        lp += (X_c[k] - X_c[i]) + (1 - U[ik] + V[ik])*R.x_max >= \
            0.5*(R.p[i]*S[i] + R.q[i]*(1 - S[i]) +
                 R.p[k]*S[k] + R.q[k]*(1 - S[k]))
        lp += (Y_c[i] - Y_c[k]) + (U[ik] + 1 - V[ik])*R.y_max >= \
            0.5*(R.p[i]*(1 - S[i]) + R.q[i]*S[i] +
                 R.p[k]*(1 - S[k]) + R.q[k]*S[k])
        lp += (Y_c[k] - Y_c[i]) + (2 - U[ik] - V[ik])*R.y_max >= \
            0.5*(R.p[i]*(1 - S[i]) + R.q[i]*S[i] +
                 R.p[k]*(1 - S[k]) + R.q[k]*S[k])
    """ Within the Enveloping Rectangle """
    for i in rect_keys:
        lp += x >= X_c[i] + 0.5*(R.p[i]*S[i] + R.q[i]*(1 - S[i]))
        lp += y >= Y_c[i] + 0.5*(R.p[i]*(1 - S[i]) + R.q[i]*S[i])
        lp += X_c[i] >= 0.5*(R.p[i]*S[i] + R.q[i]*(1 - S[i]))
        lp += Y_c[i] >= 0.5*(R.p[i]*(1 - S[i]) + R.q[i]*S[i])

    # print("\nConstraints:")
    # for name, constraint in lp.constraints.items():
        # print(name+':', constraint)

    # Solve Model
    try:
        if show_detail:
            print('\n========== Solving ==========')
        s = lp.solve(GLPK_CMD(msg=False))
        sol_dict = {1: 'Optimal', 2: 'Not Solved',
                    3: 'Infeasible', 4: 'Unbounded', 5: 'Undefined'}
        if show_detail:
            if 1 <= s <= 5:
                print("Solver status:", sol_dict[s])
            else:
                print(f"Solver status: {s}")
    except Exception as e:
        print("model.solve() has raised an ERROR:", e)

    # Print Solution
    x = value(x)
    y = value(y)
    X_c = np.array([value(X_c[i]) for i in rect_keys])
    Y_c = np.array([value(Y_c[i]) for i in rect_keys])
    S = np.array([value(S[i]) for i in rect_keys])
    U = np.array([value(U[i]) for i in comb2_keys])
    V = np.array([value(V[i]) for i in comb2_keys])
    tx = np.array([value(tx[i]) for i in abs_aux_keys])
    ty = np.array([value(ty[i]) for i in abs_aux_keys])
    wx = np.array([value(wx[i]) for i in abs_aux_keys])
    wy = np.array([value(wy[i]) for i in abs_aux_keys])
    if show_detail:
        print("\n========== Result ==========")
        # print(f'S = {S}')
        # print(f'U = {U}')
        # print(f'V = {V}')
        # print(f'tx = {tx}')
        # print(f'ty = {ty}')
        # print(f'wx = {wx}')
        # print(f'wy = {wy}')
        # print(f'Xc = {X_c}')
        # print(f'Yc = {Y_c}')
        print(f'Objective Func  = {value(lp.objective)}')
        print(f'x = {x}')
        print(f'y = {y}')
        print(f'Enveloping Area = {x*y}')
    if graph_out is False:
        return x, y

    # plt.figure(figsize=(5, 5))
    fig, ax = plt.subplots()
    for i in rect_keys:
        ax.add_patch(patches.Rectangle(
            (X_c[i] - 0.5*(S[i]*R.p[i] + (1-S[i])*R.q[i]),
             Y_c[i] - 0.5*(S[i]*R.q[i] + (1-S[i])*R.p[i])),
            S[i]*R.p[i] + (1-S[i])*R.q[i],
            S[i]*R.q[i] + (1-S[i])*R.p[i],
            edgecolor='blue',
            fill=False))
        plt.text(X_c[i], Y_c[i], str(i+1),
                 ha='center', va='center')
    ax.add_patch(patches.Rectangle(
                (0, 0), x, y,
        edgecolor='red',
        fill=False))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(title, fontsize=20)
    plt.axis('equal')
    tt = title.replace(':', '_')
    plt.savefig(f'{tt}.png')
    plt.show()

    # fig2, ax2 = plt.subplots()
    # ax2.plot(a, log_a, '.')
    # ax2.plot(b, log_b, '.')
    # ax2.legend(['ln(a)', 'ln(b)'])
    # ax2.grid('on')
    # plt.show()
    return None


if __name__ == '__main__':
    print('Please Open "Cutting_Stock.ipynb".')
    # Define Rectangles
    # R = Rects()

    # Handout Example
    # R.add(33, 10)
    # R.add(30, 11)
    # R.add(25, 15)
    # R.add(18, 14)
    # R.add(18, 10)
    # !!!!
    # R.x_max = 50
    # R.y_max = 40

    # Test
    # R.add(1, 20)
    # R.add(10, 1)

    # Assignment3 Problem
    # R.add(8, 16, 4)
    # R.add(9, 9, 5)
    # R.add(18, 3, 3)

    # Assignment3 Mod. Problem
    # R.add(8, 16, 1)
    # R.add(9, 9, 1)
    # R.add(18, 3, 3)

    # Cutting_Stock(R, 10, True)
    # t = []
    # t.append(timeit.Timer(Cutting_Stock(R, 3)).timeit(number=2))
    # print(timeit.timeit(Cutting_Stock(R, 3),
    #       setup="from __main__ import Cutting_Stock"))
    # print(t)
