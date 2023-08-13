n = int(input("Enter a number? "))

i = 0

# while i < n:
#     print("meow")
#     i += 1

list = []

print(len(list))

# len(pass list name) length of list

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
    list.append(n * i)


print(list)
