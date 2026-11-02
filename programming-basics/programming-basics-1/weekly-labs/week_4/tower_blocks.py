"""
    Author: Nazar Mykhailyshchuk
    Game "Tower Blocks"
"""

point = 15
k = 1
bin_start = ""
bin_block = ""

start = input()
for i in range(9):
    if start[i] == ".":
        bin_start += "0"
    elif start[i] == "#":
        bin_start += "1"
bin_start = int(bin_start, 2)

while point > 0:
    block = input()
    for i in range(9):
        if block[i] == ".":
            bin_block += "0"
        elif block[i] == "#":
            bin_block += "1"
    bin_block = int(bin_block, 2)

    if (bin_block ^ bin_start).bit_count() == 0:
        k += 1
        bin_start = bin_block
    else:
        if (bin_block ^ bin_start).bit_count() == 2:
            k += 1
            point -= 1
            bin_start = bin_block
        elif (bin_block ^ bin_start).bit_count() == 4:
            k += 1
            point -= 2
            bin_start = bin_block
        else:
            point -= 3
    bin_block = ""
print(k)
