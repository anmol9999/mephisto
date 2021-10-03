

content = '''Hunting is the practice of seeking, pursuing and capturing or killing wildlife or feral animals.'''


vowels = "aeiou"

for vowel in vowels:
    c = content.casefold().count(vowel)

    print(f' {vowel} -> {c} times')