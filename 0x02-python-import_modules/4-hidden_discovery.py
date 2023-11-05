#!/usr/bin/python3
# get the variables names from a compiled file
if __name__ == "__main__":
    import sys
    import imp
    module = imp.load_compiled('hidden_4', 'hidden_4.pyc')
    names = dir(module)
    names = names.sort()
    for name in names:
        if (name[:2] == __):
            continue
        print(name)
