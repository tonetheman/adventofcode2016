
import re

def supportSSL(s):
    B = re.compile(r"\[.*?\]")
    ABA = re.compile(r"(.)(.)\1")
    not_brackets = B.split(s)
    brackets = B.findall(s)

    for ts in brackets:
        ts = ts[1:-1]
        match_value = ABA.search(ts)
        if match_value is None:
            continue
        match_value = match_value.group(0)
        outside_char = match_value[0]
        inside_char = match_value[1]
        if outside_char == inside_char:
            continue
        print "checking", inside_char+outside_char+inside_char
        for tts in not_brackets:
            if tts.find(inside_char+outside_char+inside_char)!= -1:
                return True

    return False


"""
print supportSSL("aba[bab]xyz")
print supportSSL("xyx[xyx]xyx")
print supportSSL("aaa[kek]eke")
print supportSSL("zazbz[bzb]cdb")
"""

data = open("input.txt","r").readlines()
import string
data = map(string.strip,data)

count = 0
for d in data:
	if supportSSL(d):
		count = count + 1
print count
