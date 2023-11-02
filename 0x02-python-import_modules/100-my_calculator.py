#!/usr/bin/python3
if __name__ == "__main__":
    """Simple dynamic calculator"""
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {}".format(a, op, b, result))
