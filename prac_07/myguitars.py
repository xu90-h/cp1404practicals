from guitar import Guitar

def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    print("These are my guitars:")
    display_guitars(guitars)

def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display a list of Guitar objects with numbering."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

main()
