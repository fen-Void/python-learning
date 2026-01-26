# Example 2: Ticket Price Calculator (Age + Membership)

# ge = int(input("Age bata: "))
# is_member = input("Gym/Cinema member hai? (yes/no): ").lower() == "yes"

# if age >= 18:
#     if is_member:
#         print("Adult member → Ticket ₹150")
#     else:
#         print("Adult non-member → Ticket ₹250")
# else:
#     if is_member:
#         print("Child member → Ticket ₹80")
#     else:
#         print("Child non-member → Ticket ₹120")


# Number Category Checker (Nested)

num = int(input("Enter your No: "))

if num > 0 :
    if num%2==0:
        print("Positive Even")
    else:
        print("Positive odd")
elif num <0 :
    if num%2==0:
        print("Negative even")
    else:
        print("Negative odd")

else:
    print ("Zero")