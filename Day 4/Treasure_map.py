line1 = ['■', '■', '■']
line2 = ['■', '■', '■']
line3 = ['■', '■', '■']
map = [line1, line2, line3]
print("Hiding your treasure ? 'X' mark to the place.")
position = input("Give the position like rows are in letter from A and columns are in numbers from 1(B2,C1....)\n")
letter = position[0].lower()
abc = ['a', 'b', 'c']
row_index = abc.index(letter)
column_index = int(position[1]) - 1
map[row_index][column_index] = 'X'
print(f"{line1}\n{line2}\n{line3}")    