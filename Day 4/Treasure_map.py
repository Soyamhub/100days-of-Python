line1 = ['■', '■', '■']
line2 = ['■', '■', '■']
line3 = ['■', '■', '■']
map = [line1, line2, line3]
print("Hiding your treasure ? 'X' mark to the place.")
position = input("Give the position like rows are in letter from A and columns are in numbers from 1(B2,C1....)\n")
letter = position[0].lower()
row = ['a', 'b', 'c']
if letter == row[0]:
    map[0][int(position[1])] = 'X'
elif letter == row[1]:
    map[1][int(position[1])] = 'X'    
else:
    map[2][int(position[1])] = 'X'
print(f"{line1}\n{line2}\n{line3}")    