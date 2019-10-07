import sys
#import argparse

def main(args, n):
    numberlists = []
    for inputfile in args[-1*n:]:
        with open(inputfile, 'r') as f:
            numbers = f.read().split('\n')
            a = len(numbers)
            if numbers[a-1] == '':
                numbers.remove('')
            numberlists.append(numbers)

    print(numberlists)




def check_input_args(args):

    if len(args) == 1:
        raise Exception("no arguments")

    if args[1] == '-i' or args[1] == '-s':
        if args[2][-4:] == '.txt':
            pass
        else:
            raise Exception("wrong arguments")
    else:
        if args[1] == '-a' or args[1] == '-d':
            if args[3][-4:] == '.txt':
                pass
            else:
                raise Exception("wrong arguments")

    if args[1] == '-i' or args[1] == '-s':
        n = len(args) - 3
        if n == 0:
            raise Exception("wrong arguments")
        for arg in args[-1*n:]:
            if arg[-4:] != '.txt':
                raise Exception("wrong arguments")
    if args[1] == '-a' or args[1] == '-d':
        n = len(args) - 4
        if n == 0:
            raise Exception("wrong arguments")
        for arg in args[-1*n:]:
            if arg[-4:] != '.txt':
                raise Exception("wrong arguments")

    return n


if __name__ == "__main__":
    #args = argparse.ArgumentParser()
    #ap.add_argument("-b", required=False, default='-a')
    #ap.add_argument("-a", required=False, default='-a')
    args = sys.argv
    main(args, check_input_args(args))
