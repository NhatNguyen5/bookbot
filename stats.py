#Function to get text from the book
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

#Function to count the number of words
def get_num_words(str):
    return len(str.split())

#Function to count each character appeared
def count_alpbt(str):
    ret_counts = {}
    for c in str:
        c_lower = c.lower()
        if c == "\n": c_lower = "\\n" #display end line as '\n'
        if c == " ": c_lower = "\' \'" #display space as ' '
        if c_lower not in ret_counts:
            ret_counts[c_lower] = 1 #if a character not in the dictionary, initialize
        else:
            ret_counts[c_lower] += 1 #if a character is in the dictionary, increment by 1
    return ret_counts

#Helper function for .sort()
def sort_on(items):
    return items["num"]

#Function to sort the list of character counted
def sort_char_pairs(str_dict):
    ret_list = []
    for item in str_dict:
        char_pair = {}
        char_pair["char"] = item
        char_pair["num"] = str_dict[item]
        ret_list.append(char_pair)
    ret_list.sort(reverse=True, key=sort_on)
    return ret_list
