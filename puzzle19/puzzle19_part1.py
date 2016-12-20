
TOTAL_ELVES = 5

def take_present_from(n):
	return (n+1)%TOTAL_ELVES

loot = {}
for i in range(TOTAL_ELVES):
	loot[i] = 1

count = 0
ce = 0
while True:
	count = count + 1

	if count > 9:
		break

	if loot[ce]==0:
		print "elf",ce+1, "has no presents and is skipped"
		ce = (ce + 1) % TOTAL_ELVES
		continue

	victim = take_present_from(ce)
	print "elf",ce+1, "takes from ", victim+1

	loot[ce] = loot[ce] + loot[victim]

	print "SETTING victim to 0", loot[victim]
	loot[victim] = 0

	ce = (ce + 1) % TOTAL_ELVES

print "loot",loot



