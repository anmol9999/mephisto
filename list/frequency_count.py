x = '''The character begins as an extremely talented but egotistical surgeon who loses 
the ability to operate after a car crash severely damages his hands beyond repair. Searching the globe for healing, he encounters the Ancient One,
the Sorcerer Supreme. Strange becomes his student, and learns to be a master of both the mystical and the martial arts. He acquires an assortment of mystical objects, including the powerful Eye of Agamotto and Cloak of Levitation, and takes up residence in a mansion referred to as t
he Sanctum Sanctorum, 
located in 177A Bleecker Street, Greenwich Village, New York City.
Strange assumes the title of Sorcerer Supreme and, with his friend and valet Wong, defends
the world from mystical threats.'''

words = x.split()


max_freq = 0
mx_occ_word = ''

for item in words:
    count = words.count(item)
    print(f'{item} -> {words.count(item)}')
    if count > max_freq:
        max_freq = count
        mx_occ_word = item


print(f'{mx_occ_word} =>>> {max_freq}')
