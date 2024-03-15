filename = "books/frankenstein.txt"

with open (filename) as f:
    # Reading the file and counting the words
    content = f.read()
    words = content.split()
    count = len(words)
    print (f"---Begin report of {filename} ---\n {count} words found in the document\n")

    # Function to lower the case of text
    def lowered_text(text):
        return text.lower()
    lowered_content = lowered_text(content)
    
    # Function to count letters    
    def count_letters(text):
        char_count = {}
        for char in text:
            if char.isalpha():  # Checks if a character is from alphabet
                if char in char_count:
                    char_count[char] += 1  # if character is present, increment the count
                else:
                    char_count[char] = 1   # if character is not present, set the count to 1
        return char_count
    letter_frequency = count_letters(lowered_content)
    

    def dict_to_lists(char_count):
        list_of_dicts = []
        # Move items from dictionary to the list of dictionaries
        for char in char_count:
            new_dict = {'character': char, 'count': char_count[char]}
            list_of_dicts.append(new_dict)
        return list_of_dicts
   
   
    # Function to sort dictionary based on count
    def sort_on(dict):
        return dict["count"]
    
    
    list_of_dicts = dict_to_lists(letter_frequency) # Convert dictionary to list
    list_of_dicts.sort(key=sort_on, reverse=True) # Sort list by count in reverse order

    
    # Output the final report
    for dict_item in list_of_dicts:
        print(f"Character: {dict_item['character']}, Count: {dict_item['count']}")
    
    
