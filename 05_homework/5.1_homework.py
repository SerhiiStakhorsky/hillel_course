import string
import keyword

user_variable_name = input("Print text: ")
punctuation = string.punctuation.replace("_", "")
banned_keywords = keyword.kwlist
has_double_underscore = user_variable_name.count("__") >= 1 and user_variable_name.strip("_") == ""

negative_contractions = [
    user_variable_name[0].isdigit(),
    any(char.isupper() for char in user_variable_name),
    any(char in punctuation for char in user_variable_name),
    user_variable_name in banned_keywords,
    " " in user_variable_name
]

if has_double_underscore or any(negative_contractions):
    print(False)
else:
    print(True)
