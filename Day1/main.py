import urllib.request  # the lib that handles the url stuff

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = "<fill this>"

url = "https://adventofcode.com/2024/day/1/input"
headers = {
    "Cookie": f"session={SESSION_COOKIE}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URLError: {e.reason}")

lines = data.splitlines()

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
