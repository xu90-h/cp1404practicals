# Question 1: Write name to name.txt
name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()