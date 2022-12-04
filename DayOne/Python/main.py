# 2D list where each sublist represents one elf
elves = [[]]
# Using a counter to keep track of what elf we're currently loading
elfCounter = 0

# Load in all elves
with open('../SampleFiles/real_file.txt', 'r') as f:
    for line in f:
        # Removing all Control Characters / whitespace
        strippedLine = line.strip()
        # If the line is empty then move on to the next elf
        if strippedLine == '':
            elfCounter += 1
            elves.append([])
            continue
        # Making the assumption that a line contents are always an integer
        elves[elfCounter].append(int(strippedLine))

elfSums = []
for elf in elves:
    elfSums.append(sum(elf))

print('(Part One) Total Calories of Elf carrying the most: ' + str(max(elfSums)))

sortedElves = sorted(elfSums, reverse=True)
print('(Part Two) Sum of Top 3 Elves: ' + str(sum(sortedElves[:3])))
