
def part1(input):
    for i in input:
        for j in input:
            if int(i)+int(j) == 2020:
                print(int(i)*int(j))
                return

def part2(input):
    for i in input:
        for j in input:
            for k in input:
                if int(i)+int(j)+int(k) == 2020:
                    print(int(i)*int(j)*int(k))
                    return

input = open("/home/jrajasansir/git/aoc-q-2020/input/day-1.data").readlines()

part1(input)
part2(input)
