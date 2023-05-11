import re

list = ["cid", "Carys", "David"]
list_of_cool = []
names = ""
user = ""

while user != "done":
    user = input("Who in the list? ")

    for names in list:
        pattern = re.compile(user)
        matches = pattern.finditer(names)
        if matches:
            list_of_cool.append(names)

print(list_of_cool)



