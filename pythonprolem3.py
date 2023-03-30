""""
python practice problem3 Food and calories
you visit a restrurant called codewithpradeep and food items in this restrurant
are sorted based on their amount of calories. you have to reverse this list of
food items containing their calories
you have to use following methods to reverse to a list
- Inbuilt method of python
- list name[::-1] slicing trick
- swapping first element with the last on second element with second last one
and so on
Take a list as input from the user
[5,4,1]
output:
[5,4,1]
[5,4,1]
[5,4,1]
All three methods give same results
"""
print("welcome to codewithpradeep Restrurant\n")
food_items = []
for i in range(3):
    food_items.append(input())
# food_items.append(input())
# food_items.append(input())
print(food_items)
food_items.reverse()
print(food_items)
for i,j in [(0,2)]:
    food_items[i],food_items[j] = food_items[j],food_items[i]

# temp = food_items[0]
# food_items[0] = food_items[2]
# food_items[2] = temp
print(food_items)