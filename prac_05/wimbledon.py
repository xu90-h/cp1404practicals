"""
Wimbledon
Estimate: 20 minutes
Actual:    minutes
"""

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
