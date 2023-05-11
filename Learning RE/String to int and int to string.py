#String to Int

solvethis = "32 + 698"

splitted = solvethis.split(" ")
first = splitted[0]
op = splitted[1]
second = splitted[2]
final =  int(first) + int(second)

# print(final)

x = eval(solvethis)
# print(x)

# --------------------------------------------------------

#Int to String

solvethis2 = 32 + 698

print("32 + 698 = " + str(solvethis2))




