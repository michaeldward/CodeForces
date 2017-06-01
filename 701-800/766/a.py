a = raw_input()
b = raw_input()

def get_all_substrings(input_string):
 	length = len(input_string)
 	return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

def compare(a, b):
	#if a != b: #strings are different
	#	return max(len(a), len(b))
	#elif a == b:
	#	return -1
	longest = 0
	aa = get_all_substrings(a)
	bb = get_all_substrings(b)
	qq = set(aa).symmetric_difference(set(bb))
	if (len(qq) == 0):
		return -1
	else:
		return len(max(qq, key=len))

print compare(a, b)