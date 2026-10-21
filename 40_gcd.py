"""Program 40: Find the Greatest Common Divisor (GCD)."""


def gcd(a, b):
    """Calculate the greatest common divisor of two integers using the Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("GCD:", gcd(num1, num2))
