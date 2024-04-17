txt = "The best things in life are free!"
print(txt)
inputtext = input("Search text:")
if inputtext in txt:
  print("Yes, '" + inputtext + "' is present.")
else:
    print("No, '" + inputtext + "' is not present.")