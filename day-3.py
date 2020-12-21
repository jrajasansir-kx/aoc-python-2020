from functools import partial


def part1(input):
    print(find_trees(input, 1, 3))

def part2(input):
    moveFunc = partial(find_trees, input)

    slopes = [ (1,1), (1,3), (1,5), (1,7), (2,1) ]

    result = 1

    for slope in slopes:
        result *= moveFunc(slope[0], slope[1])

    print(result)

def find_trees(input, yMove, xMove):
    x, trees = 0, 0

    xLength = len(input[0]) - 1

    for yc in range(yMove, len(input), yMove):
        x+=xMove

        if input[yc][x % xLength] == '#':
            trees+=1
    
    print(yMove, xMove, trees)

    return trees


input = open("/home/jrajasansir/git/aoc-q-2020/input/day-3.data").readlines()

part1(input)
part2(input)