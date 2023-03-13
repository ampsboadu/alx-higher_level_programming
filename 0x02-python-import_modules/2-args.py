#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    
    if count == 0:
        print("{:d} arguments.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))

    i = 1;
    while i <= count:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1
