# Sorted Squared Array
# Write a function that takes in a non-empty array of integers 
# that are sorted in ascending order 
# and returns a new array of the same length 
# with the squares of the original integers also sorted in ascending order.

# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]
# Sample Input
# array = [-10, -7, -4, 1, 2, 3, 5, 6, 8, 9]
# [100, 49, 16, 1, 4, 9, 25, 36, 64, 81]
# Sample Output
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def sorted_squared_array(array):
  return sorted(list(map(lambda num:num**2, array)))

# def sorted_squared_array(array):
#   negative_list = []
#   positive_list = []
#   for n in array:
#     if n < 0:
#       negative_list.insert(0, n**2)
#     else:
#       positive_list.append(n**2)
  
#   newlist = []
#   while positive_list and negative_list:
#     if positive_list[0] < negative_list[0]:
#       newlist.append(positive_list.pop(0))
#     else:
#       newlist.append(negative_list.pop(0))

#   while positive_list:
#     newlist.append(positive_list.pop(0))
  
#   while negative_list:
#     newlist.append(negative_list.pop(0))

#   return newlist

array = [1, 2, 3, 5, 6, 8, 9]
for _ in range(555555):
  sorted_squared_array(array)
print(sorted_squared_array(array))
array = [-10, -7, -4, 1, 2, 3, 5, 6, 8, 9]
print(sorted_squared_array(array))
