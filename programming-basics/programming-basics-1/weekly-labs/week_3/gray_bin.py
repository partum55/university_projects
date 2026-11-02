gr_code = input()

bit_len = len(gr_code)
bin_code = int(gr_code[0])

for i in range(1, bit_len):
    if gr_code[i] == '0':
        bin_code = (bin_code << 1) | (bin_code & 1)
    else:
        bin_code = (bin_code << 1) | (~bin_code & 1)

print(f'{bin_code:0{bit_len}b}')
