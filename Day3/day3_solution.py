import url_parser.url_parser as parser
import re

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = ""
data = parser.getDataFromURL("https://adventofcode.com/2024/day/3/input", SESSION_COOKIE)

# https://adventofcode.com/2024/day/3
expressions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

sum = 0
for e in expressions:
    left, right = map(int, e[4:len(e)-1].split(','))
    sum += int(left) * int(right)

print(f"Day 3, part 1, sum of multiplications: {sum}")

# https://adventofcode.com/2024/day/3#part2
expressions = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", data)

sum = 0
do = True
for e in expressions:
    if e == "do()":
        do = True
    elif e == "don't()":
        do = False
    elif do:
        left, right = map(int, e[4:len(e)-1].split(','))
        sum += int(left) * int(right)

print(f"Day 3, part 2, sum of multiplications: {sum}")