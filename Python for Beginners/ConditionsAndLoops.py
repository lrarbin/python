word = input("Please enter a four-letter word: ")
word_length = len(word)
if word_length == 4:
    print(word, "is a four-letter word. Well done.")
elif word_length == 3:
    print(word, "is a three-letter word. Try again.")
else:
    print(word, "is not four-letter word. Dumb ass.")

x = 1
while x < 10:
    print(x)
    x= x+1

words = ["Cat", "Dog", "Unicorn"]

for word in words:
    print(word)

for x in range (1, 10):
    print(x)