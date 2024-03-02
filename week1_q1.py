

#1 Write a function count_vowels(word)
#that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    vowels = [o, u, a, i, e]
    count = 0
    for var in word:
        if var.lower() in vowels:
            count += 1
    return count
