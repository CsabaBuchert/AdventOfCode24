import url_parser.url_parser as parser

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = ""
lines = parser.getLinesFromURL("https://adventofcode.com/2024/day/1/input", SESSION_COOKIE)

numbers1 = []
numbers2 = []

for idx, line in enumerate(lines):
    first, second = map(int, line.split())
    numbers1.append(first)
    numbers2.append(second)

numbers1.sort()
numbers2.sort()

n_of_lines = min(len(numbers1), len(numbers2))

# https://adventofcode.com/2024/day/1#part1
distance = 0
for idx in range(n_of_lines):
    distance += abs(numbers2[idx] - numbers1[idx])

print(f"Day one, part one, total distance: {distance}")

#https://adventofcode.com/2024/day/1#part2
similarity_score = 0
for idx in range(n_of_lines):
    similarity_score += numbers1[idx] * numbers2.count(numbers1[idx])

print(f"Day one, part two, similarity score: {similarity_score}")
