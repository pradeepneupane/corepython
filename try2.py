
try:
    f = open("pradeep.txt")
    f1 = open("does.txt")

except IOError as e:
    print("print iof error is comming", e)

# except Exception as e:
#     print(e)

else:
    print("This will run only  if except is not running")

finally:
    print("Run this anyaway")
    f.close()

print("Important stuff")