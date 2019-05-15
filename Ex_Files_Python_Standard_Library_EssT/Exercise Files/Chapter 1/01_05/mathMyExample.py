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

