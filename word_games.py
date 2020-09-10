with open("scrabble.txt", 'r') as f:
    count = 0
    for line in f:
        if count > 5:
            break
        print(line)
        count += 1