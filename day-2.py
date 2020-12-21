from collections import Counter


def part1(input):
    valid = 0

    for line in input:
        split = line.split(' ')
        range = [int(str2int) for str2int in split[0].split('-')]
        char = split[1][0:1]
        toCheck = split[2]

        if range[0] <= Counter(toCheck)[char] <= range[1]:
            valid+=1
    
    print(valid)

def part2(input):
    valid = 0

    for line in input:
        split = line.split(' ')
        range = [int(str2int) for str2int in split[0].split('-')]
        char = split[1][0:1]
        toCheck = split[2]

        if (toCheck[range[0] - 1] == char) ^ (toCheck[range[1] - 1] == char):
            valid+=1
    
    print(valid)

input = open("/home/jrajasansir/git/aoc-q-2020/input/day-2.data").readlines()

part1(input)
part2(input)