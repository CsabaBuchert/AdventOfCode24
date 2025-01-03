import url_parser.url_parser as parser
from functools import cmp_to_key

# open url, press f12, switch to network tab, check input file, headers, copy cookie/session
SESSION_COOKIE = "53616c7465645f5f53804a4951342c163e051d91bbd5cddff0813cc3e1c7ad0cbb10665bca2affd5afb38e7020cd5ec4a63a31486699f9aafed613dbb81d8357"
data = parser.getDataFromURL("https://adventofcode.com/2024/day/5/input", SESSION_COOKIE)

test_data = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"

# https://adventofcode.com/2024/day/5
def parseData(data: str) -> tuple:
    page_rules = {}
    updated_pages = []

    data = data.split("\n\n")
    for rule in data[0].split("\n"):
        key, value = map(int, rule.split("|"))
        if key not in page_rules:
            page_rules[key] = []
        page_rules[key].append(value)
    for l in map(str, data[1].split("\n")):
        if l != '':
            updated_pages.append(list(map(int, l.split(","))))

    return page_rules, updated_pages

#page_rules, updated_pages = parseData(test_data)
page_rules, updated_pages = parseData(data)

def checkRules(page_rules, pages):
    for page_idx in range(len(pages) - 1):
        if pages[page_idx] not in page_rules:
            return False
        rules = page_rules[pages[page_idx]]
        remaining_pages = pages[page_idx + 1:]
        if len(set(remaining_pages).intersection(rules)) != len(remaining_pages):
            return False
    return True

def calculateTotal(updates):
    total = 0
    for pages in updates:
        if len(pages) % 2 == 1:
            mid_index = len(pages) // 2
            total += pages[mid_index]
    return total

valid_updates = []
invalid_updates = []
for pages in updated_pages:
    if checkRules(page_rules, pages):
        valid_updates.append(pages)
    else:
        invalid_updates.append(pages)

print(f"Day 5, part 1, sum of valid lines: {calculateTotal(valid_updates)}")

# https://adventofcode.com/2024/day/5#part2

def compare(a, b, rules):
    if a in rules and b in rules[a]:
        return -1
    return 1

def fixPageOrdering(page_rules, pages):
    pages.sort(key=cmp_to_key(lambda a, b: compare(a, b, page_rules)))
    return pages

fixed_updates = []
for pages in invalid_updates:
    fixed_updates.append(fixPageOrdering(page_rules, pages))

print(f"Day 4, part 2, sum of fixed lines: {calculateTotal(fixed_updates)}")
