import numpy as np
import math 
x1=float(input("enter first component of first vector"))
y1=float(input("enter second component of first vector"))
x2=float(input("enter first component of second vector"))
y2=float(input("enter second component of second vector"))
vector=np.array([x2-x1,y2-y1])
magnitude=np.linalg.norm(vector)
print("Magnitude=", magnitude)
