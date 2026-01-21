# # string = input("Enter: ")
# # new_string = string[22:27 + 1]
# # new_string2 = string[97:102 + 1]
# # print(new_string, new_string2 )

# # infile = open('stringsAndLists.txt')
# # string1 = infile.readline()
# # string2 = infile.readline()
# # string2 = string2.split(' ')
# string2 = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
# a=int(string2[0])
# b=int(string2[1])
# c=int(string2[2])
# d=int(string2[3])
# print (string1[a:b+1], string1[c:d+1])

#SUM OF ALL INTEGERS
n_1 = int(input("enter a no. "))
n_2 = int(input("enter another no. "))


if n_1%2 == 0:
    n_1 = n_1 - 1
sum_1 = n_1

while 1 < n_1 <10000 :

    sum_1 = sum_1 + n_1 - 2
    n_1 = n_1 - 2
if n_2%2 == 0:
    n_2 = n_2 - 1
sum_2 = n_2
while 1< n_2< 10000:
    sum_2 = sum_2 + n_2 - 2
    n_2 = n_2 - 2
print(abs(sum_1 - sum_2))

