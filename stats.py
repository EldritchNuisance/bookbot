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

def get_count(item):
    return item["count"]
 
def sort_on(char_dict):
    new_list = []
    for char, cnt in char_dict.items():  # Loop directly over items for clarity
        new_list.append({"character": char, "count": cnt})
    
    # Use the get_count function for the sorting key
    new_list.sort(reverse=True, key=get_count) 
    return new_list

