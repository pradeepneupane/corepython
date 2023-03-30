import time
initial = time.time()
k = 0
while(k<45):
    print("me")
    time.sleep(3)
    k+=1
print("while loop ran in", time.time()-initial, "seconds")
print()

initial2 = time.time()
for i in range(45):
    print("me")
print("for loop ran in", time.time()-initial2, "seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
