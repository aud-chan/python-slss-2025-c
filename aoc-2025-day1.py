# AOC day 1
# Author: Audrey
# 1 December


def part_one():
    cur_location = 50
    answer = 0
    # read every line in the instructions

    with open("data/aoc-2025-day1.txt")as f:
        for line in f:
        # instruction example "R10" -> right 10
            direction = line [0]
            distance = int(line[1:])
            print(direction, distance)
            # if we go right -> add
            if direction == "R":
                cur_location += distance
            # if we go left -> subtract
            elif direction == "L":
                cur_location -= distance
            print("Cur Location:", cur_location)

            # if it passes 0 during
            if



            # if we land on zero keep track of it
            str_location = str(cur_location)[-2:]
            print("Str Location:", str_location)
            if str_location == "00" or str_location == "0":
                answer += 1
            else:
                answer += 0



                print(answer)






if __name__ == "__main__":
    part_one()
