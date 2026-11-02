a, b = (int(input())), (int(input()))
ans, temp = 0, 0


temp = a ^ b
for i in range ((temp).bit_length()):
    ans += temp & 1
    temp = temp >> 1

print(ans)