from prettytable import PrettyTable
from random import random

def func(x, y, z): return round(a0+a1*x+a2*y+a3*z, 3)

def gen_X(max, round_n, size): return [round(random()*max, round_n) for i in range(size)]

def get_X0(x, round_n): return round((max(x) + min(x))/2, round_n)

def get_dx(x, x0, round_n): return round(max(x) - x0, round_n)

def get_xN(x, x0, dx, round_n): return map(lambda x: round((x-x0)/dx, round_n), x)

a0 = 1
a1 = 2
a2 = 3
a3 = 4

x1 = gen_X(20, 3, 8)
x2 = gen_X(20, 3, 8)
x3 = gen_X(20, 3, 8)
y = list(map(func, x1, x2, x3))

x01 = get_X0(x1, 3)
x02 = get_X0(x2, 3)
x03 = get_X0(x3, 3)

dx1 = get_dx(x1, x01, 3)
dx2 = get_dx(x2, x02, 3)
dx3 = get_dx(x3, x03, 3)

xN1 = get_xN(x1, x01, dx1, 3)
xN2 = get_xN(x2, x02, dx2, 3)
xN3 = get_xN(x3, x03, dx3, 3)

y_et = func(x01, x02, x03)

crit = list(map(lambda y: round((y-y_et)**2, 3), y))

mainTable = PrettyTable()
mainTable.field_names = ["№", "X1", "X2", "X3", "Y", "XN1", "XN2", "XN3", "Критерій"]
mainTable.add_rows(
    zip(range(1, 9), x1, x2, x3, y, xN1, xN2, xN3, crit)
)
mainTable.add_row(["X0", x01, x02, x03, y_et, "-", "-", "-", "-"])
mainTable.add_row(["dx", dx1, dx2, dx3, "-", "-", "-", "-", "-"])

print(mainTable)

print("Y_ет =", y_et)

ind_solve = crit.index(max(crit))
print("Функція відгуку та точка, які задовольняють критерію вибору max((Y-Y_et)^2):\nX1 = {}, X2 = {}, X3 = {}\nY = {}".format(x1[ind_solve], x2[ind_solve], x3[ind_solve], y[ind_solve]))
