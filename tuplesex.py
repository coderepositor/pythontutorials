#type_of_accounts = ("Savings",)
type_of_accounts = ("Savings","Current", "Credit", "Fixed","Credit")
print(type_of_accounts.count("Credit")) #counting specific elements inside the tuple
print(type_of_accounts[::-1]) # Reversing the tuple elements
print(len(type_of_accounts)) # counting the total number of elements inside the tuple
print(type_of_accounts.index("Current"))
print(type_of_accounts[1:3])
sorted_tuple = tuple(sorted(type_of_accounts));
print(sorted_tuple[::-1]);
print("*" * 80)
