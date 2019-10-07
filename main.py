import sys

def main(args, n):
    numberlists = []
    if n == 1:
        with open(args[-2], 'w') as f:
            with open(args[-1], 'r') as f2:
                a = f2.read()
            f.write(a)
    else:
        for inputfile in args[-1*n:]:
            with open(inputfile, 'r') as f:
                numbers = f.read().split('\n')
                a = len(numbers)
                if numbers[a-1] == '':
                    numbers.remove('')
                    a = len(numbers)
                    for i in range(a):
                        numbers[i] = int(numbers[i])
                    numberlists.append(numbers)


    print(numberlists)

    outlist = []
    i = 0
    for list in numberlists:
        if len(outlist) == 0:
            outlist.append(list[i])
        else:
            



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
    args = sys.argv
    main(args, check_input_args(args))
