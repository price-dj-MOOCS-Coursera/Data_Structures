# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def rabin_karp_matcher(pattern, text):
	"""
	Rabin-Karp from lectures and test book
	"""
	n = len(text)
	m = len(pattern)
	q = 1000000007
	d = 263
	h = pow(d, m-1) % q
	p = 0
	t = 0
	result = []
	for i in range(m):
		p = (d*p + ord(pattern[i])) % q
		t = (d*t + ord(text[i])) % q
	
	for s in range(n-m+1):
		if p == t:
			for i in range(m):
				if pattern[i] == text[s+i]:
					result.append(s)
					break
				
		if s < n-m:
			t = (t - h*ord(text[s])) % q 		# remove letter s
			t = (t*d + ord(text[s+m])) % q 		# add letter s+m
			t = (t + q) % q 					# make sure that t >= 0
	
	return result
			
			


if __name__ == '__main__':
    print_occurrences(rabin_karp_matcher(*read_input()))

