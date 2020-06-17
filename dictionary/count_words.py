def count_words():
    counts = dict()
    print("\nEnter a line of text: \n")
    line = input("")

    words = line.split()

    print("\nWords: ", words)

    print("\nCounting...")
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print("\nCounts", counts)


count_words()
