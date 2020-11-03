def longestSubseq(arr, n):

	# Stores the distinct
	# array elements
	s = set()

	# Traverse the input array
	for i in range(n):
	
		# If current element has not
		# occurred previously
		if (arr[i] not in s):

			# Insert it into set
			s.add(arr[i])

	return len(s)

# Given array
arr = "abcda"
n = len(arr)

# Function Call
print(longestSubseq(arr, n))

