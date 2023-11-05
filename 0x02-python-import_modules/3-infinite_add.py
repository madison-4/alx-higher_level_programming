#!/usr/bin/python3
# adds all the arguments it receives
# Will obviously use sys module
if __name__ == "__main__":
    import sys
    length = len(sys.argv[1:])
    result = 0
    for i in range(1, (length + 1)):
        j = int(sys.argv[i])
        result += j
    print(result)
