"""
	date:2020.04.15
	author:Derek_lws
"""
x1 = [1,3,5]
y2 = [9,12,13]
L = [ x**2 for (x,y) in zip(x1,y1) if y>10]
print(L)
