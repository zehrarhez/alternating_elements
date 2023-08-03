text = "hi my name is zehra and i am learning python"
k = range(len(text))
new_string = ""
for i in k:
    if i % 2 == 0:
        new_string += text[i].upper()
    else:
        new_string += text[i].lower()
print(new_string)


