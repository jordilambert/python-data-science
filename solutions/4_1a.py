import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("Sum of %d and %d: %d" % (x, y, x + y))
except IndexError as e:
    print("Please supply 2 command line arguments")
    print(e)
except ValueError as e:
    print("Please supply 2 integers")
    print(e)


