""" print("WELLCOME TO MY NEW JURNY") """

# print("HELLO WORLD")

# num = ["ad", "dak", "ddaa"]

# num = [14,56,74,89]

# for index, value in enumerate(num):
    # print(f"index : {index} , value : {value} ")

# def display_person(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")


# display_person(Name="Amir Khan", Age="45")


""" n = int(input())
while n:
    s = input()
    ans = []
    for i in s:
        ans.append(i)
    ans.reverse()
    for i in ans:
        print(i, end=" ")
    n-=1
    print() """


"""n = int(input())
while n:
    x, y = [int(i) for i in input().split()]
    f = min(x, y)
    l = max(x, y)
    sum = 0
    for i in range(f+1, l):
        if i % 2 == 1:
            sum+=i
    print(sum)
    n-=1"""



""" 
n = int(input())

x , y = 0, 1
for _ in range(n):
   print(x, end=" ")
   x, y = y, x+y
#    tmp = x
#    x = y
#    y = tmp+x  
"""

# S = (X0 - 1) + (X2) + (X4) + (X6) + ............... + (XN)

""" 
a, b = [int(i) for i in input().split()]
s = 0
for i in range(2, b+1, 2):
    s+=a**i
print(s)

"""

# Max Split

""" 
s = input().strip()

count = 0
substrings = []
string = ""

for char in s:
    string += char
    if char == 'L':
        count += 1
    else:
        count -= 1
    if count == 0:
        substrings.append(string)
        string = ""

print(len(substrings))
for substring in substrings:
    print(substring) 
"""

""" # Good Sequence
n = int(input())
a = [int(i) for i in input().split()]

count_dict = {}
for i in a:
    count_dict[i] = count_dict.get(i, 0)+1

ans = 0
for key , item in count_dict.items():
    if item >= key:
        ans += item - key
    else :
        ans += item
  
print(ans) """

N = int(input())
A = list(map(int, input().split()))

operations = 0

while all(num % 2 == 0 for num in A):
    A = [num // 2 for num in A]
    operations += 1

print(operations)





