import re

def num():
    chr = "ab1dc23f2g345"
    reg = "\d+"
    temp = re.findall(reg,chr)
    print(temp)

def other():
    chr = "ab1dc23f2g345"
    lis = []
    r = [str(a) for a in range(1,10)]
    index_temp = []
    for i in chr:
        if i in r:
            # lis.append(i)
            if len(lis) >= 1:
                if lis[-1] not in r:
                    lis.append(lis.pop() + i)
                else:
                    lis.append(i)
            else:
                lis.append(i)
        else:
            continue

    print(lis)

if __name__ == '__main__':
    num()
    other()

    print(sum(int(i) for i in re.findall("\d+","ab1dc23f2g345")))
    print(sum(int(i) for i in re.compile("\d+").findall("ab1dc23f2g345")))
    print(sum([int(i) for i in re.compile("\d+").findall("ab1dc23f2g345")]))