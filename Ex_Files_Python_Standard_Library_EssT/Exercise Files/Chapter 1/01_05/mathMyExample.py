import math

# https://docs.python.org/3/library/math.html

print("ceiling of")
f1 = 4.0
print(f"  math.ceil({f1}) = |{math.ceil(f1)}|")
f1 = 4.1
print(f"  math.ceil({f1}) = |{math.ceil(f1)}|")
f1 = 4.5
print(f"  math.ceil({f1}) = |{math.ceil(f1)}|")
f1 = 4.9
print(f"  math.ceil({f1}) = |{math.ceil(f1)}|")
i1 = 3
print(f"  math.ceil({i1}) = |{math.ceil(i1)}|")

print("copysign of")
a=1.0
b=-1.0
print(f"  copysign({a}, {b}) = |{math.copysign(a, b)}|")
a=-1.0
b=1.0
print(f"  copysign({a}, {b}) = |{math.copysign(a, b)}|")
a=-1.0
b=-1.0
print(f"  copysign({a}, {b}) = |{math.copysign(a, b)}|")
a=1.0
b=0.0
print(f"  copysign({a}, {b}) = |{math.copysign(a, b)}|")
a=1.0
b=-0.0
print(f"  copysign({a}, {b}) = |{math.copysign(a, b)}|")
# According to the documentation, platforms supporting signed zeros yield |-1.0|.

print("math.factorial(x)")
i=1
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=2
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=3
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=4
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=5
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=6
print(f"  math.factorial({i}) = |{math.factorial(i)}|")
i=4
j=3
print(f"  (math.factorial({i}) / math.factorial({j})) = |{(math.factorial(i) / math.factorial(j))}|")
i=5
j=2
print(f"  (math.factorial({i}) / math.factorial({j})) = |{(math.factorial(i) / math.factorial(j))}|")
i=6
j=5
k=3
print(f"  ((math.factorial({i}) - math.factorial({j}) ) / math.factorial({k})) = |{((math.factorial(i) - math.factorial(j) ) / math.factorial(k))}|")
print("\n")

print("floor of")
f1 = 4.0
print(f"  math.floor({f1}) = |{math.floor(f1)}|")
f1 = 4.1
print(f"  math.floor({f1}) = |{math.floor(f1)}|")
f1 = 4.5
print(f"  math.floor({f1}) = |{math.floor(f1)}|")
f1 = 4.9
print(f"  math.floor({f1}) = |{math.floor(f1)}|")
i1 = 3
print(f"  math.floor({i1}) = |{math.floor(i1)}|")
print("\n")

print("math.fmod(x, y)")
i=10.0
j=3.0
print(f"  math.fmod({i}, {j}) = |{math.fmod(i, j)}|")
i=10
j=3
print(f"  math.fmod({i}, {j}) = |{math.fmod(i, j)}|")
i=10.0
j=5.0
print(f"  math.fmod({i}, {j}) = |{math.fmod(i, j)}|")
i=13.0
j=7.0
print(f"  math.fmod({i}, {j}) = |{math.fmod(i, j)}|")
print("\n")

print("x % y")
i=10
j=3
print(f"  {i} % {j} = |{i % j}|")
i=10.0
j=3.0
print(f"  {i} % {j} = |{i % j}|")
i=10
j=5
print(f"  {i} % {j} = |{i % j}|")
i=13
j=7
print(f"  {i} % {j} = |{i % j}|")
# even though % may have identical result in many cases, 
# math.fmod(a, b) is preferred for floats, and
# a % b is preferred for integers.
# [see https://docs.python.org/3/library/math.html :: math.fmod(x, y)] 
print("\n")

print("math.frexp(x)")
# Okay, this is lower level stuff... given a float, express its internal representation:
# First its multiplier, the mantissa, and second its exponent which the base, 2, is raised to.
# This is used to “pick apart” the internal representation of a float in a portable way.
f = 10.24
print(f"  math.frexp({f}) = |{math.frexp(f)}|")   # math.frexp(10.24) = |(0.64, 4)|
f = 1024.0
print(f"  math.frexp({f}) = |{math.frexp(f)}|")   # math.frexp(1024.0) = |(0.5, 11)|
print(f"  0.5 * 2**11 = |0.5 * {2**11}|")   # 0.5 * 2**11 = |0.5 * 2048|
print(f"  0.5 * 2**11 = |{0.5 * 2**11}|")   # 0.5 * 2**11 = |1024.0|
f = 102.4
print(f"  math.frexp({f}) = |{math.frexp(f)}|")   # math.frexp(102.4) = |(0.8, 7)|
print(f"  0.8 * 2**7 = |0.8 * {2**7}|")   # 0.8 * 2**7 = |0.8 * 128|
print(f"  0.8 * 2**7 = |{0.8 * 2**7}|")   # 0.8 * 2**7 = |102.4|
f = 3.1415
print(f"  math.frexp({f}) = |{math.frexp(f)}|")   # math.frexp(3.1415) = |(0.785375, 2)|
print(f"  0.785375 * 2**2 = |0.785375 * {2**2}|")   # 0.785375 * 2**2 = |0.785375 * 4|
print(f"  0.785375 * 2**2 = |{0.785375 * 2**2}|")   # 0.785375 * 2**2 = |3.1415|
# print("\n")

