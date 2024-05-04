import string

user_input = input("Write text: ")

symbols_to_remove = string.punctuation
text_without_symbols = user_input
for symbol in symbols_to_remove:
    text_without_symbols = text_without_symbols.replace(symbol, "")

text_with_replace_and_is_title = text_without_symbols.title().replace(" ", "")

add_hashtag = "#" + text_with_replace_and_is_title
print(add_hashtag[:140])
