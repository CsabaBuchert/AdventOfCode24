import url_parser.url_parser as parser

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = ""
data = parser.getLinesFromURL("https://adventofcode.com/2024/day/4/input", SESSION_COOKIE)

# https://adventofcode.com/2024/day/4
def count(key: str, y: int, x: int, offset_x: int, offset_y: int) -> int:
    n_of_matches = 0
    substring = ""
    for _ in range(len(key)):
        if 0 <= y < len(data) and 0 <= x < len(data[y]):
            substring += data[y][x]
        y += offset_y
        x += offset_x
    if substring == key:
        n_of_matches += 1
    return n_of_matches
    
n_of_xmas = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'X':
            for offset_x in range(-1, 2):
                for offset_y in range(-1, 2):
                    if offset_x != 0 or offset_y != 0:
                        n_of_xmas += count("XMAS", y, x, offset_x, offset_y)

print(f"Day 4, part 1, number of xmas: {n_of_xmas}")

# https://adventofcode.com/2024/day/4#part2
def countCrossWords(key: str, y: int, x: int) -> bool:
    if len(key) % 3 != 0:
        return 0

    if 1 <= y < len(data) - 1 and 1 <= x < len(data[y]) - 1:
        substring1 = data[y - 1][x - 1] + data[y][x] + data[y + 1][x + 1]
        substring2 = data[y - 1][x + 1] + data[y][x] + data[y + 1][x - 1]
        return (substring1 == key or substring1 == key[::-1]) and (substring2 == key or substring2 == key[::-1])
    return False

n_of_xmas = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'A' and countCrossWords("MAS", y, x):
            n_of_xmas += 1

print(f"Day 4, part 2, number of x-mas: {n_of_xmas}")