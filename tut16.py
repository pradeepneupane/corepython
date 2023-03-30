# #for loops in python
# list1 = [["pradeep", 1], ["harry", 2], ["carry", 3], ["larry", 4]]
# # print(list1[0], list1[1], list1[2], list1[3])
# dict1 = dict(list1)
# for item in dict1:
#     print(item)
# # print(dict1)
# # for item, lollypop in dict1.items():
# #     print(item, "and lollypop is", lollypop)

nam = ["p", 1, "R", 7, "A", 9, "D", 11]
for item in nam:
    if str(item).isnumeric() and item>6:
        print(item)