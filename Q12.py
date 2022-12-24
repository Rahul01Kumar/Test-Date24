class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i, c in enumerate(s):
            if c == ' ':
                k -= 1
            if k == 0:
                return s[:i]
        return s
def BalancedPartition(str1, n):

	if (n == 0):
		return 0

	r = 0
	l = 0

	ans = 0

	for i in range(n):
	
		if (str1[i] == 'R'):
			r += 1

		elif (str1[i] == 'L'):
			l += 1

		if (r == l):
			ans += 1

	return ans

if __name__ == '__main__':
	
	str1 = "LLRRRLLRRL"
	n = len(str1)

	# Function call
	print(BalancedPartition(str1, n))


