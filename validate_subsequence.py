# Given two non-empty arrays of integers, 
# write a function that determines 
# whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers 
# that aren't necessarily adjacent in the array 
# but that are in the same order as they appear in the array. 
# For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], 
# and so do the numbers [2, 4]. 
# Note that a single number in an array and the array itself 
# are both valid subsequences of the array.

# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# Sample Output
# true

def validate_subsequence(array, sequence):
  seqIdx = 0
  for i in range(len(array)):
    if array[i] == sequence[seqIdx]:
      seqIdx += 1
      if seqIdx == len(sequence):
        return True
  return False

array = [1, 2, 3, 4]
sequence = [1, 3, 4]
print(validate_subsequence(array, sequence))
sequence = [2, 4]
print(validate_subsequence(array, sequence))
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(validate_subsequence(array, sequence))
sequence = [1, 6, -1, 10, 11]
print(validate_subsequence(array, sequence))
sequence = [-1]
print(validate_subsequence(array, sequence))
sequence = [5, 1, 22, 25, 6, -1, 8, 10]
print(validate_subsequence(array, sequence))