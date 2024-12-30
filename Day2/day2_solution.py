import url_parser.url_parser as parser

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = ""
lines = parser.getLinesFromURL("https://adventofcode.com/2024/day/2/input", SESSION_COOKIE)

# https://adventofcode.com/2024/day/2

def is_increasing(e: list[int]):
    return all(e[i] < e[i + 1] for i in range(len(e) - 1))

def is_decreasing(e: list[int]):
    return all(e[i] > e[i + 1] for i in range(len(e) - 1))

def adjacent_diff_is_between(e: list[int], min: int, max: int):
    return all(min < abs(e[i] - e[i + 1]) < max for i in range(len(e) - 1))

def isSafe(e):
    return (is_increasing(elements) or is_decreasing(elements)) and adjacent_diff_is_between(elements, 0, 4)
n_of_safe_lines: int = 0

for idx, line in enumerate(lines):
    elements = list(map(int, line.split()))
    if isSafe(elements):
        n_of_safe_lines += 1

print(f"Day 2, part 1, number of safe lines: {n_of_safe_lines}")

# https://adventofcode.com/2024/day/2#part2
def isSafe(e: list[int], handle_error: bool):
    n_of_increases = 0
    n_of_decreases = 0
    n_of_wrong_steps = 0

    for idx in range(1, len(e)):
        # check wrong increases
        if e[idx] > e[idx - 1]:
            n_of_increases += 1

        # check wrong decreases
        if e[idx] < e[idx - 1]:
            n_of_decreases += 1

        diff = abs(e[idx] - e[idx - 1])
        if diff == 0 or diff > 3:
            n_of_wrong_steps += 1

    if (n_of_increases == 0 or n_of_decreases == 0) and n_of_wrong_steps == 0:
        return True

    if handle_error:
        for idx in range(len(e)):
            temp = e[:]
            del temp[idx]
            if isSafe(temp, False):
                return True
    
    return False

n_of_safe_lines = 0
for idx, line in enumerate(lines):
    elements = list(map(int, line.split()))
    if isSafe(elements, True):
        n_of_safe_lines += 1

print(f"Day 2, part 2, number of safe lines: {n_of_safe_lines}")