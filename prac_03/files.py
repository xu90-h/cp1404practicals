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

# Question 3: Read first two numbers from numbers.txt and sum them
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)

# Question 4: Sum all numbers in numbers.txt
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)