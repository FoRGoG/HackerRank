import cmath

'''general solution'''
data = input().strip()
r = abs(complex(float(data[0]), float(data[2])))
f = cmath.phase(complex(float(data[0]), float(data[2])))
print(r)
print(f)

'''clean solution'''
data = complex(input().strip())
result = cmath.polar(data)
print(result[0])
print(result[1])