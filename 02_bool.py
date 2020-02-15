import random

a = [False, True, True, None, True, None, None, False, False, None, True, False]
b = ["or", "or", "or", "==", "!=", "==", "and", "==", "!=", "and", "==", "or"]
c = [False, False, None, None, True, True, False, True, None, False, True, None]

for i in range(len(a)):
    print(str(a[i]) + " " + b[i] + " " + str(c[i]))
    eval(str(a[i
