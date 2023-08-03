people = ["zehra", "ayşe", "fatma", "ahmet", "mehmet"]

A = []
B = []

# printing the names without index value
for person in people:
    print(person)
print("----")
# printing the names with index value
for index, person in enumerate(people):
    print(index, person)
    if index % 2 == 0:
        A.append(person)
    else:
        B.append(person)
print(A)
print(B)
