import string

def encode(input, shift):
	lower = list(string.ascii_lowercase)
	upper = list(string.ascii_uppercase)
	special = list(string.punctuation)

	encrypted = ""

	for each in input:
		if each in lower:
			eachindex = lower.index(each)
			encrypted += lower[(eachindex+int(shift))%len(lower)]
		if each in upper:
			eachindex = upper.index(each)
			encrypted += upper[(eachindex+int(shift))%len(upper)]
		if each in special:
			eachindex = special.index(each)
			encrypted += special[(eachindex+int(shift))%(len(special))]

	return encrypted


print(encode("Mr. Baez", 13))
