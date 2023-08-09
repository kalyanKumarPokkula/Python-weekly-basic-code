# *****
# *****
# *****
# *****
# *****

n = int(input("Enter a number?"))

i = 0

while i < n:
    j = 0
    while j < n:
        print("* ", end="")
        j += 1
    print("")
    i += 1

print("")

k = 0

while k < n:
    j = 0
    while j <= k:
        print("* ", end="")
        j += 1
    print("")
    k += 1

print("")

while n > 0:
    j = 0
    while j < n:
        print("* ", end="")
        j += 1
    print("")
    n -= 1
