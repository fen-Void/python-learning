# Example 2: Ticket Price Calculator (Age + Membership)

age = int(input("Age bata: "))
is_member = input("Gym/Cinema member hai? (yes/no): ").lower() == "yes"

if age >= 18:
    if is_member:
        print("Adult member → Ticket ₹150")
    else:
        print("Adult non-member → Ticket ₹250")
else:
    if is_member:
        print("Child member → Ticket ₹80")
    else:
        print("Child non-member → Ticket ₹120")