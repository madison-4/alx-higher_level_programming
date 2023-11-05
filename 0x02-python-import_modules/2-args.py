#!/usr/bin/python3
# print arguments given to script
# Will obviously use sys module
if __name__ == "__main__":
    import sys
    length = len(sys.argv[1:])
    if (length == 0):
        print("{:d}: arguments.".format(length))
        sys.exit()
    elif (length == 1):
        print(f"{length:d} argument:")
        print(f"1: {sys.argv[1]}")
        sys.exit()
    else:
        print(f"{length:d} arguments:")
        for i in range(1, (length + 1)):
            print(f"{i:d}: {sys.argv[i]}")
