import string
import keyword

user_variable_name = input("Print text: ")
punctuation = string.punctuation.replace("_", "")
banned_keywords = keyword.kwlist

negative_contractions = [
    user_variable_name[0].isdigit(),
    any(char.isupper() for char in user_variable_name),
    any(char in punctuation for char in user_variable_name),
    user_variable_name in banned_keywords,
    " " in user_variable_name
]
if any(negative_contractions):
    print(False)
else:
    print(True)
