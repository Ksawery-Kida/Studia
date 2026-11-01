movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f"Title in capital letters: {movie.upper()}")

# print title in small letters
print(f"Title in small letters: {movie.lower()}")

# print how many times the vowel "e" appears in the title
count = 0 
for c in movie:
    if c == 'e':
        count += 1
print(f'The letter \'e\' appears {count} times in the title')

# print where in the text is the word "Lord"
print(f"The word 'lord' appears in the title: {'lord' in movie.lower()}")

# print where in the text is the word "dragon"
print(f"The word 'dragon' appears in the title: {'dragon' in movie.lower()}")

