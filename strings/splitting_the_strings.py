msg = "we will be seeing the horizon"

words = msg.split()
print(words)


msg2 = "hi there, how are you? where have you been?"
sentence = msg2.split(",")
print(sentence)


sentence = msg2.split("?")
print(sentence)


gibberish = msg2.split('a')
print(gibberish)

sentence = msg2.split(" ")
print(sentence)


print(f"we found {len(words)} words")

print(f"we found {len(msg2.split())} words in msg2")

