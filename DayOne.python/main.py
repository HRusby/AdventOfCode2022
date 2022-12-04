elves = [[]]
elfCounter = 0

# Load in all elves
with open('./SampleFiles/real_file.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            elfCounter += 1
            elves.append([])
            continue
        elves[elfCounter].append(int(line.strip()))

elfSums = []
for elf in elves:
    elfSums.append(sum(elf))

print('Part 1, Total Calories of Elf carrying the most: ' + str(max(elfSums)))

sortedElves = sorted(elfSums, reverse=True)
print('Part 2, Sum of Top 3 Elves' + str(sum(sortedElves[:3])))
