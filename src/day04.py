"""
	date:2020.04.16
	author:Derek_lws
"""
import numpy as np#Numpy是Python的一种开源的数值计算扩展。
#主要用于储存和处理大型矩阵
import random
a = [random.uniform(100.0,200.0) for i in range(50)]#返回50个100.0-200.0之间的浮点数
for x in a:
	print(x)
print(np.eye(2, dtype=int))#返回一个二维数组
