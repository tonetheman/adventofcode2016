
data = open("input3.txt","r").readlines()
import string
data = map(string.strip,data)

good_count = 0
def check(d):
	global good_count

	good = True
	if d[0] + d[1] > d[2]:
		print "ok"
	else:
		good = False
	if d[1]+d[2] > d[0]:
		print "ok"
	else:
		good = False
	if d[0]+d[2] > d[1]:
		print "ok"
	else:
		good = False


	if good == False:
		pass
	else:
		good_count = good_count + 1

print data
total_len = len(data)
print total_len
rp = 0
while True:
	for i in range(rp,rp+3):
		data[i] = data[i].split()
		data[i] = map(int,data[i])
	group1 = [data[rp][0],data[rp+1][0],data[rp+2][0]]
	group2 = [data[rp][1],data[rp+1][1],data[rp+2][1]]
	group3 = [data[rp][2],data[rp+1][2],data[rp+2][2]]

	print group1,group2,group3

	check(group1)
	check(group2)
	check(group3)

	rp = rp + 3
	if rp==total_len:
		break



print "good count", good_count
