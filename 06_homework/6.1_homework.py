import string
def characters_between(char1, char2):
    all_letters = string.ascii_letters
    start_index = all_letters.index(char1)
    end_index = all_letters.index(char2)
    result = all_letters[start_index:end_index+1]
    return result

user_input = input("Enter two letters devided by '-': ")
char1, char2 = user_input.split('-')
print(characters_between(char1, char2))
