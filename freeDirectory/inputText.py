txt = "The best things in life are free!"
print(txt)
inputtext = input("Search text:")
if inputtext in txt:
  print("Yes, '" + inputtext.capitalize() + "' is present.")
else:
    print("No, '" + inputtext.capitalize() + "' is not present.")