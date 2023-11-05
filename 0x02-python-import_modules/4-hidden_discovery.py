#!/usr/bin/python3
# get the variables names from a compiled file
if __name__ == "__main__":
    import hidden4
    names = dir(hidden4)
    names = filter(lambda x: not x.startswith('__'), names)
    names= names.sort()
    for name in names:
        print(name)
