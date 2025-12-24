def get_word_count(text):
    count_ = text.split()  ## a v c c a d a
    count_len=  len(count_)
    return count_len

def get_char_count (text):
    lowercase = text.lower()
    char_dict= {}
    for char in lowercase:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1 
    return char_dict

def sort_helper(dict_item):
    return dict_item["num"]    

def get_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char":char,"num":count})
    char_list.sort(key=sort_helper, reverse=True)
    return char_list