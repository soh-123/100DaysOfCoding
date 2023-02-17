# write a program that will mark a spot with an X. As if it's the place to hide your treasure on the map using map coordinations
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

vertical = int(position[0])
horizontal = int(position[1])

map[vertical-1][horizontal-1] = "💎"

print(f"{row1}\n{row2}\n{row3}")

