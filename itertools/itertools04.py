Still takes some time for me to recall this information.
"|" for collecting items from both groups (similar to OR)
"&" to pick only those, who are at both in same time (similar to AND)
"-" is in first, not in second
"^" only in one group, not in both (similar to NOT AND)

# (1)
What is the result of this code?
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))
#                               Answer(-) #2

# (2)
What is the result of this code?
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

# Explination:
# is based on recursion principle....
# Consider the power(2,3) function.
# For the first call the value will be power(2,3).
# Thus at the end of first iteration the return value will be 2*power (2,2).
# For the second call x remains same while y decreases 
# by 1 so it will proceed as power(2,2).
# Now the return value will be {2*power(2,1)} 
# which will be substituted in the place of power(2,2) in first iteration.
#  In third call function arguments are power(2,1).
# Similarly the return value will be {2*power (2,0)}
# which will be substituted in the place of power(2,1).
# Finally the function call will be power(2,0) 
# which covers the base case of y==0.
# Thus the return value will be 1. This will take the place of power(2,0).
# Now taking all the return values in one equation 
# we will get {2*2*2*1} which is equal to 8.

#                               Answer(-) #8

# (3)
Fill in the blanks to calculate the expression x*(x+1) 
using an anonymous function and call it for the number 6.

a = (_______ x: x(x+1))____
# a = (lambda x: x*(x+1))(6)
print(a)

# (4)

Fill in the blanks to leave only even numbers in the list.

nums = [1, 2, 8, 3, 7]
res = list(_____(x: x %__ == 0, nums))
# res = list(filter(x:x % 2 == 0, nums))
print(res)

#(5)
Drag and drop from the options below to print only the items 
in the set "a" that are not in the set "b".
print(_ _ _)
#print(a - b)

# some time for me to recall this information.
# "|" for collecting items from both groups (similar to OR)
# "&" to pick only those, who are at both in same time (similar to AND)
# "-" is in first, not in second
# "^" only in one group, not in both (similar to NOT AND)