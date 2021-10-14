# This file is a running note section for CPSC 222
#https://stackoverflow.com/questions/19085807/please-enter-a-commit-message-to-explain-why-this-merge-is-necessary-especially
import math
import random

'''
print("Please enter the voltage: ")
voltage = input()
voltage = float(voltage)

print("Please enter the resistance: ")
resistance = input()
resistance = float(resistance)

voltageSq = math.pow(voltage, 2)
power = voltageSq/resistance
print("The power is ", power )

x = 6

if x == 6:
     print("x is 6")
else:
     print("x is not 6")

x = -5

if x < 0:
    print("x is negative")
elif x > 0:
    print("x is greater than 0")
else:
    print("x is 0")

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")
print()

for character in "hello":
    print(character, end=" ")
print()

for i in range(9):
    print(i, end=" ")
print()

for i in range(4, 9):
    print(i, end=" ")
print()

for i in range(0, 11, 2):
    print(i, end=" ")
print()

for i in range (8, 3, -2):
    print(i, end=" ")
print()

for i in range(0, 44, 2):
    if i == 40:
        print(i, end=" ")
        break
    print(i, end=", ")
print()

k = 0

while k <= 40:
    print(k, end=", ")
    k += 2
print()
while True:
    user_input = input("Enter 'Quit' to quit ")
    if user_input == "Quit":
        break
print("Loop exited")

die_roll = random.randrange(1, 7)
print(die_roll, end=" ")
print()

die_roll = random.randint(1, 6)
print(die_roll, end=" ")

#random.seed(0) good for reproducibility, fills the table with a constant

def say(message):
    print(message)

say("hi there")
say("go zags!")
say("Im evading my taxes and submitting a false annual income to the IRS!")

def compute_circle_area(radius):
    area = math.pi * radius ** 2
    print("area: ", area)

compute_circle_area(50)

def compute_with_returns(radius):
    area = math.pi * radius ** 2
    return area

circle_area = compute_with_returns(25)
print(circle_area)

def compute_circle_area_and_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = compute_circle_area_and_circumference(5)

#can also load them into a list called tuple, but the list is immutable

area_and_circumference = compute_circle_area_and_circumference(5)

num_list = []
i = 0

while i < 20:
    num_list.append(random.randrange(1, 11, 1))
    print(num_list[i], end=" ")
    i += 1

def bogoSort(a):
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)

def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

print()
bogoSort(num_list)
print(num_list, end=" ")

#Just me messing around, there are built in functions to sort lists.


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums, "\nPlease enter the value [0, 10] you would like to remove")
remove = int(input())

if not remove in nums:
    print("Not in list try again bozo")
else:
    while remove in nums:
        nums.remove(remove)
print(nums)

list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_two = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def contains(list_one, list_two):
    same_first_ele = False
    same_last_ele = False

    if len(list_one) and len(list_two) > 0:
        if list_one[0] == list_two[0]:
            same_first_ele = True
        if list_one[-1] == list_two[-1]:
            same_last_ele = True
        
    return same_first_ele, same_last_ele

same_first_ele, same_last_ele = contains(list_one, list_two)
print(same_first_ele, same_last_ele)
same_first_ele, same_last_ele = contains([0,1,2], [1,2,3])
print(same_first_ele, same_last_ele)


winter = ["snow", "christmas"]
#print(winter)
winter.append("santa is coming")
#print(winter)
winter.extend(["he is displeased", "every moment you are not running he is getting closer"])
#print(winter)
winter += ["he has arrived", "obliteration"]
#print(winter)
first_word = winter.pop(0)
#print(winter)
winter_list = ["Step 1: Wake up ", "Step 2: Go downstairs to your loving family ", "Step 3: Where are t̴͓͑͒̐̈́̑̓͠h̵̨̡̧̧̼͈̦̣̜͖͖̯͍̞͂̓̔̈́̓̐̆͝ę̸̳͔͕̰̪̳̺͛̇̌̏̓́̇͐̑̚̕͝͝ý̶̧̭̥̦̻͍͙̥̻͍̙̰̘̜͛̒̌̈̈́͘͝ ̴͓̣͇̎͒̑̂̿̽a̷̧̩̦͚͐̅͑̎̓̐́̏̾̀̀̊͘͘͜͝ŕ̷͙́̋͗̊̌͐̌̓̚̕̕e̶̬̥̰̹̥̰͈̗̳̯̪̯͙͆̆͐̀̈́̈͌̓ͅ ̶̡͎͈̅͌̕̚͝ḩ̶̢̞̘͖͙̗̟̤̘̺̀͆͑͊̉̾͊͒̕͜ȩ̸̛̛͚̥̫̳̪̭͓̤̖̦̺̣͑̓͗͌͐̀̌̔͗̂̇r̸̟̺̲̻͕̫̞̠̅̉̆̋͛̎͜͠ē̴̢̞͉̝̖̠̒ ", "Step 4: 1994 Santa Claus is Coming to Town Incident "]

comma_separated_string_of_values = "a,b,c,d"
values_list = comma_separated_string_of_values.split(",")
print(values_list)

print("jesus didnt memorize the bible")
'''

def print_data(data):
    for row in data:
        for value in row:
            print(value, end="\t")
        print()

data = []

for i in range(10):
    row = []
    for j in range(5):
        rand_num = random.randint(1,10)
        row.append(rand_num)

    data.append(row)

#print(num_list)

print_data(data)

smallest_ele = largest_ele = data[0][0]

for row in data:
    if min(row) < smallest_ele:
        smallest_ele = min(row)
    if max(row) > largest_ele:
        largest_ele = max(row)

print(smallest_ele, largest_ele)

count = 0
found = False
user_value = int(input("Please enter a number between 1-10 inclusive to remove from that stinky list : "))
for row in data:
    while user_value in row:
        row.remove(user_value)
        found = True
        count += 1
if found:
    print("count: ", count)
    print_data(data)
else:
    print("yo number aint here g get out of here")



    