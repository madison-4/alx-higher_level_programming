#!/usr/bin/python3
# get the variables names from a compiled file
if __name__ == "__main__":
    import sys
    import imp
    module = imp.load_compiled('hidden_4', 'hidden_4.pyc')
    names = dir(module)
    names = filter(lambda x: not x.startswith('__'), names)
    names = names.sort()
    for name in names:
        print(name)
