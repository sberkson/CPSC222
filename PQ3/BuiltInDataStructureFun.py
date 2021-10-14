#Sam Berkson
#PQ3
#9/20/21

nums = [3, 6, -1, 7, 9, 7]

print(nums)
print(nums[0], nums[-6], nums[0:2]

nums.append(100)
print(nums)
nums.remove(7)
print(nums)

print(nums)
nums.sort()
print(nums)

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]

print(matrix[0][0])
print(matrix[1][2])

matrix = [[1, 2, 3] [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))
print(type(matrix[0][0]))

cube = [[[0, 0], [1, 1]], [2, 2], [3, 3]]]
print(cube[0][0][0])

my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))

my_single_item_tuple = (1, )
print(my_single_item_tuple)

my_empty_tuple = tuple()
print(my_empty_tuple)

my_dict = {}
my_empty_dict = dict()
print(my_dict)
my_dict["12345"] = "Jane Doe"
print(my_dict)

state_capitals = {"Washington": "Olympia", "Ohio": "Columbus", :"Best NFL Team": "Cleveland Browns"}
print(state_capitals)
state_capitals["California"] = "Sacremento"
print(state_capitals)

roman_numerals = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50)])
print(roman_numerals)
roman_rumerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

print(len(state_capitals))

print("Washington" in state_capitals)
print("Olympia" in state_capitals.values())

for state in state_capitals:
    print(state, state_capitals[state])

for (state, capital) in state_capitals.items():
    print(state, "*", capital)

