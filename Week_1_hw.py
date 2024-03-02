'''
Week 1 Data Science Bootcamp
'''

#1 Write a function count_vowels(word)
#that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    vowels = [o, u, a, i, e]
    count = 0
    for var in word:
        if var in vowels:
            count += 1

    return count


#2 Iterate through the following list of animals and print each one in all caps.
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for item in animals:
    print(item.capital) #something


#3 Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for num in range(1, 21):
    if num%2 == 0:
        type = "This number is even"
        print(num, type)
    else:
        type = "This number is odd"
        print(num, type)

#Write a function sum_of_integers(a, b) that takes
#two integers as input from the user and returns their sum.

def sum_of_integers(a, b):
    return a+b



'''
Additional Challenge - Books data challenge
'''
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]

def check_rating(book):
    for item in books:
        if books.get("title") == book:
            if books.get("rating") > 4.5:
                return "high"
            elif books.get("rating") <= 4.0:
                return "low"
            else:
                return "medium"

def average_rating_by_genre(books, genre):
    total = 0
    for item in books:
        for key in items:
            if genre not in key:
                return "This genre is not available"
        if books.get("title") in books:
            total += books.get("rating")
    return total//












        
            
        
        
        



