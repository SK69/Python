# reading a list of words and returning the length of the longest word
# the list shouldn't exceed more than 10 items and each item should have a minimum of 2 and max of 8 characters

while True:
    n = int(input("Enter the number of words"))
    if n < 10:
        break

maxlen = 0

while n >= 1:
    print("Enter word number ")
    word = str(input())
    print("max= ", maxlen, "n= ", n)
    if 2 <= len(word) <= 8 and len(word) > maxlen:
        max = len(word)
        print(n)
        words = word
        n -= 1

print("The word ", words, " is of length ", max, " and is the largest")
