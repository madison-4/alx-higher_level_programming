#!/usr/bin/python3
# get the variables names from a compiled file
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    names = names.sort()
    for name in names:
        if (name[:2] == "__"):
            continue
        print(f"{name:s}")
