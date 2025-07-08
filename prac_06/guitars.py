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

    guitars.append(Guitar("Fender Stratocruisers", 2014, 765.40 ))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars: ")

        for i, guitar in enumerate(guitars, 1):
            # enumerate object
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :(Quick, go and buy one!)")

main()