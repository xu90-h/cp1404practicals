"""
Wimbledon
Estimate: 20 minutes
Actual:    minutes
"""


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)

    country_to_wins = count_wins_by_country(data)
    unique_champions = get_unique_champions(data)

    print("Wimbledon Champions:")
    for country, wins in sorted(country_to_wins.items()):
        print(f"{country} {wins}")

    print(f"\nThese {len(unique_champions)} countries have won Wimbledon:")
    print(", ".join(unique_champions))

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip header
        data = []
        for line in file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


def count_wins_by_country(data):
    """Return a dictionary mapping countries to number of wins."""
    country_to_wins = {}
    for row in data:
        country = row[2]
        if country in country_to_wins:
            country_to_wins[country] += 1
        else:
            country_to_wins[country] = 1
    return country_to_wins


def get_unique_champions(data):
    """Return a sorted list of unique champion names."""
    champions = set()
    for row in data:
        champion = row[1]
        champions.add(champion)
    return sorted(champions)

main()