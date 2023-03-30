""""'
Harry porter got n number of apple. Harry has some students among whom, he wants to distribute the apples. These n
number of apples are provided to harry by his friend and he can request for few more or few less apples.
you need to print wheather the number is a divisor or not.
Input:
take input from n, mn and mx from the user
output:
print wheather the numbers between mn and mx are divisor or not
Example:
If n is 20 and mn = 2 and mx = 20
2 is the divisor of 20
3 is the divisor of 20
............
5 is the divisor of 20
"""
n = int(input("Enter the no of apple that harry got to distribute\n"))
mn = int(input("Enter the minimum number\n"))
mx = int(input("Enter the maximum number\n"))
for i in range(mn,mx+1):
    if n%i==0:
        print(f"{i} is the divisor of {n}\n")
    else:
        print(f"{i} isnot the divisor of {n}\n")

