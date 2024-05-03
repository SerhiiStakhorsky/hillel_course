import string

user_input = input("Write text: ")
text_with_replace_and_is_title = user_input.title().replace(" ", "")

symbols_to_remove = string.punctuation
text_without_symbols = text_with_replace_and_is_title
for symbol in symbols_to_remove:
    text_without_symbols = text_without_symbols.replace(symbol, "")

add_hashtag = "#" + text_without_symbols
print(add_hashtag[:140])
