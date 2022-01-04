import numpy as np
from matplotlib import markers, pyplot as plt


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
    # repeat the first point to create a 'closed loop'
    polygen = np.array([[0, 0], [4, 0], [4, 3], [2, 6], [0, 6], [0, 0]])
    xp, yp = zip(*polygen)
    f_polygen = [[3*x + 5*y, 2*x + 4*y] for x, y in polygen[0:-1]]
    sort_f = np.sort(f_polygen, axis=0)
    print(f'f_polygen       : {f_polygen}')
    print(f'sorted f_polygen: {sort_f.tolist()}')
    fx, fy = zip(*f_polygen)  # Drop point E (not on edge)
    xx, yy = feasible_area(200, 200)  # Feasilbe Area points
    fxx = []
    fyy = []
    for _x, _y in zip(xx, yy):
        fxx.append(3*_x + 5*_y)
        fyy.append(2*_x + 4*_y)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8), tight_layout=True)
    ax1.set_title('Decision Variable Space', fontsize=24, fontweight='bold')
    ax1.plot(xx, yy, '.', c="gray", markersize=1)
    ax1.plot(xp, yp, '.-', markersize=17)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    # Constraints
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

    ax2.set_title('Objective Function Space', fontsize=24, fontweight='bold')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.plot(fxx, fyy, '.', c='#BFBFBF', markersize=1)
    ax2.plot(fx[0:-1], fy[0:-1], '.-', markersize=17)
    ax2.plot(fx[-1], fy[-1], '.', markersize=17)
    # Points label
    ax2.text(1, 0.2, f'$A\'({fx[0]},{fy[0]})$', va='center', fontsize=20)
    ax2.text(12, 6, f'$B\'({fx[1]},{fy[1]})$', va='center', fontsize=20)
    ax2.text(27, 18, f'$C\'({fx[2]},{fy[2]})$', fontsize=20)
    ax2.text(33, 27, f'$D\'({fx[4]},{fy[4]})$', ha='right', fontsize=20)
    ax2.text(29, 24, f'$E\'({fx[3]},{fy[3]})$', ha='right', fontsize=20)
    # axis, aspect
    ax2.set_xlabel('$f_1 (max)$', fontsize=20)
    ax2.set_ylabel('$f_2 (min)$', fontsize=20)
    plt.savefig('ASGMT_04/P1-1_Graphic Solution_area.png')
    plt.show()
