
# def fib():
#     a=1
#     b= 1
#     k = int(input("enter no. of offspring: "))
#     n = int(input("enter the no. of months: "))

#     print (a)
#     print(b)

#     for i in range(3, n+1):
#         c = a + k*b
#         b = a
#         a = c
        
       
#         print(c)

# fib()
#ATTEMPT NO. 1
# n = int(input("enter: "))

# a = 1
# b = 1
# print("1")
# print("1")
# while a < n:
#     s = a + b
#     print(s)
#     a = s + b
#     print(a)
#     b = s + a
#     print(b)

#ATTEMPT NO. 2
first = 1
last = 1
for i in  range(5, 3):
    sum = first + last
    first = last 
    last = sum
    
print(last)