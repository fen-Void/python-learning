# Q1
# for i in  range (1 , 6):
#     print(i)

#Q2

# i = 11

# while  i >= 1:
#     print(i)

#     i = i-1

#Q3
# a = int(input("Enter ur number:"))
# for i in range(1 ,11):
#     print(a*i) 

#Q4 1 se 20 tak sirf even numbers print karo


# for i in range(1 ,21):
#     if (i%2==0):
#         print(i)

######################  Pro tip 

# for i in range(2, 21 ,2):
#     print(i)

#Q6  sum of no 

# a = int(input("Enter ur no"))
# sum = 0

# for i in range (1 , a+1):
#     sum += i

# print("Total sum :" ,sum)

#Q5 Uska table reverse order mein print karo

# a = int(input("Enter ur number : "))
# for i in range (10 , 0 , -1):
#   print (i * a)


#Q^ factorial 

a  = int(input("Enter ur no : "))
fac = 1

for i in range (1 , a+1):
    fac *= i
print (fac)