#proper noun 
def find_index_words(text):
    words = text.split()
    index_words = []
    count = 1
    
    for word in words:
        if word[0].isupper() and word.isalpha():
            index_words.append((word, count))
        count += 1
    
    if len(index_words) == 0:
        print("None")
    else:
        for index_word in index_words:
            print(f"{index_word[1]} : {index_word[0]} ")

text = input("Enter the text: ")
find_index_words(text)