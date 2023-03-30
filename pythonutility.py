import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        if args.y == 0:
            return "division by zero is not possible"
        return args.x / args.y

    else:
        return "Invalid operator. Please use 'add', 'mul', 'sub' or 'div'."

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first number.")
    parser.add_argument('--y', type=float, default=3.0, help="Enter second number.")
    parser.add_argument('--o', type=str, default="add", help="Enter operator (add, mul, sub, div).")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

