# Question 1: Write name to name.txt
name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Question 2: Read name from name.txt and greet
file = open('name.txt', 'r')
name = file.read()
print(f"Hi! {name}")
file.close()

