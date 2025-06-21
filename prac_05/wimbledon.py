"""
Wimbledon
Estimate: 20 minutes
Actual:    minutes
"""


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)

    champions = count_champions(data)
    countries = extract_countries(data)

    print("Champions and number of wins:")
    for champion, wins in champions.items():
        print(f"{champion}: {wins}")

    print("\nCountries in alphabetical order:")
    countries_sorted = sorted(countries)
    print(", ".join(countries_sorted))

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # 跳过表头行
        data = []
        for line in file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

def count_champions(data):
    champions = {}
    for row in data:
        champion = row[1]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions

def extract_countries(data):
    countries = set()
    for row in data:
        country = row[2]
        countries.add(country)
    return countries

main()