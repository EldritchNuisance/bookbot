def word_count(string):
    words = string.split()
    return len(words)

#Counting character by iterating through a string
def char_count(string):
    count = {}
    lower = string.lower()
    for char in lower:
        if char in count:
           count[char] += 1
        else:
            count[char] = 1
    return count   
