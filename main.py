import sys
import time

def main(args, nf, dataType, sortType):
    start_time = time.time()
    numberlists = []
    if nf == 1:
        with open(args[-2], 'w') as f:
            with open(args[-1], 'r') as f2:
                a = f2.read()
            f.write(a)
    else:
        for inputfile in args[-1*nf:]:
            with open(inputfile, 'r') as f:
                numbers = f.read().split('\n')
                a = len(numbers)
                if numbers[a-1] == '':
                    numbers.remove('')
                a = len(numbers)
                if dataType == 1:
                    for i in range(a):
                        numbers[i] = int(numbers[i])
                numberlists.append(numbers)


        #print(numberlists)

        outlist = []
        im = 0
        i = 0
        ex = False
        t = 0
        while ex !=True:
            if i == len(numberlists):
                im += 1
                i = 0
            for list in numberlists:
                lout  = len(outlist)
                if lout == 0:
                    outlist.append(list[im])
                else:
                    n = 0
                    try:
                        while True:
                            if list[im] <= outlist[n]:
                                outlist.insert(n,list[im])
                                break
                            elif list[im] > outlist[n]:
                                n += 1
                            if n == lout:
                                outlist.append(list[im])
                                break
                            t = 0
                    except:
                        t += 1
                        if t == len(numberlists):
                            ex = True
                i += 1

        #print(outlist)
        if sortType == '-a':
            with open(args[-nf - 1], 'w') as f:
                for i in outlist:
                    if dataType == 1:
                        f.write(str(i))
                    else:
                        f.write(i)
                    f.write('\n')
        else:
            with open(args[-nf - 1], 'w') as f:
                for i in range(len(outlist) - 1, -1, -1):
                    if dataType == 1:
                        f.write(str(outlist[i]))
                    else:
                        f.write(outlist[i])
                    f.write('\n')
    print("--- %s seconds ---" % (time.time() - start_time))



def check_input_args(args):
    dataType = 0
    sortType = '-a'
    if len(args) == 1:
        raise Exception("no arguments")

    if args[1] == '-i' or args[1] == '-s':
        if args[1] == '-i':
            dataType = 1
        else:
            dataType = 0
        if args[2][-4:] == '.txt':
            pass
        else:
            raise Exception("wrong arguments")
    else:
        if args[1] == '-a' or args[1] == '-d':
            if args[2] == '-i':
                dataType = 1
            else:
                dataType = 0
            if args[1] == '-d':
                sortType = '-d'
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

    return n, dataType, sortType

if __name__ == "__main__":
    args = sys.argv
    nf, dataType, sortType= check_input_args(args)
    main(args, nf, dataType, sortType)
