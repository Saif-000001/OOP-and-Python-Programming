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



n = int(input())

x , y = 0, 1
for _ in range(n):
   print(x, end=" ")
   x, y = y, x+y
#    tmp = x
#    x = y
#    y = tmp+x 


