User_name = input("Enter the name: ")  # This should print "Enter the name:"

if len(User_name) >= 3:
    print(f'Hello {User_name}, How are you?')
else:
    print("Please enter a name with more than 3 letters.")