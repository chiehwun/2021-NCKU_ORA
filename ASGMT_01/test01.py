import numpy as np
from matplotlib import pyplot as plot
import pulp
import platform
import sys

print("Platform   :", platform.platform())
print("Python ver.:", platform.python_version())
print("PuLP ver.  :", pulp.__version__)
# pulp.pulpTestAll()

###### Problem 1 ######
# 建立一個新的model，命名為model
model = pulp.LpProblem("cost_minimize", pulp.LpMinimize)

#  pulp.LpVariable()加入變數
a = pulp.LpVariable('a', lowBound=2, cat='Integer')
b = pulp.LpVariable('b', lowBound=0, cat='Integer')
c = pulp.LpVariable('c', lowBound=0, cat='Integer')
d = pulp.LpVariable('d', lowBound=0, cat='Integer')
e = pulp.LpVariable('e', lowBound=0, cat='Integer')
f = pulp.LpVariable('f', lowBound=0, cat='Integer')

# model += 設置目標函數
model += 5*a+4*b+7*c+8*d+15*e+35*f, 'Cost'

# model += 加入限制式
model += 70*a+100*b+50*c+60*d+150*e+100*f <= 600, 'Con1'
model += 70*a+100*b+50*c+60*d+150*e+100*f >= 400, 'Con2'
model += 11*a-45*b+15*c-2*d-25*e+30*f >= 0, 'Con3'
model += 3*c+2*e+120*f >= 60, 'Con4'
model += 3*a+4*b+d+2*e+f >= 12, 'Con5'
model += b-2*c >= 0, 'Con6'
model += e+f >= 1, 'Con7'

# mmodel.solve()求解'
model.solve()
print("DDDDDDDDDDDDDDDDD")

# 透過屬性varValue,name顯示決策變數名字及值
for v in model.variables():
    print(v.name, "=", v.varValue)

# 透過屬性value(model.objective)顯示最佳解
print('obj=', pulp.value(model.objective))
