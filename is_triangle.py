"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false
in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

# Triangle Inequality Theorem: the sum of any two sides must be strictly greater than the third side ((a+b>c,a+c>b,b+c>a)


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
