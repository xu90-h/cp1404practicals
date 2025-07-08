from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost) # Create guitar object
        guitars.append(guitar_add) # Add object into guitar list
        print(f"{guitar_add} added.")
        name = input("Name: ")



main()