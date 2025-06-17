"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""

def main():
    text = input("Text: ")
    words = text.split()

    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    sorted_words = sorted(word_to_count.keys())
    max_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")

main()