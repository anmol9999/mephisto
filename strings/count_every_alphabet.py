from string import ascii_lowercase


content = '''Hunting is the practice of seeking, pursuing and capturing or killing wildlife or feral animals.'''


num_of_a = content.count('a')
print(f'a occurs {num_of_a} times')

in_counter = content.count('in')
print(f'`in` occurs {in_counter} times')

# counting all alphabets

max_freq = 0
most_freq_letter = ''

for letter in ascii_lowercase:
    counter = content.casefold().count(letter)
    print(f'{letter} found {counter} times')
    if max_freq < counter:
        max_freq = counter
        most_freq_letter = letter


print(f"the {most_freq_letter} has highest frequency: {max_freq}")