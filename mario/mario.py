import cs50

while True:
    height = cs50.get_int("Height: ")
    if height > 0 and height < 9:
        break

block = 1

for i in range(height):
    for space1 in range(height - block):
        print(" ", end="")
    for block1 in range(block):
        print("#", end="")
    print(" ", end="")
    for block2 in range(block):
        print("#", end="")
    print("")
    block += 1