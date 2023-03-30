# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
# print(ls)

# dict1 = {i:f"item{i}" for i in range(100) if i%3==0}
# print(dict1)

# dict1 = {i:f"item{i}" for i in range(5)}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

# dresses = {dresses for dresses in["dresses1","dresses2","dresses1","dresses2"]}
# print(dresses)
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
print(evens)
print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
for item in evens:
    print(item)




