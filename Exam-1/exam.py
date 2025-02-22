def decimal_to_binary(dec_num):
    if dec_num == 0:
        return "0"
    bin_num = ""
    while dec_num > 0:
        bin_num = str(dec_num % 2) + bin_num
        dec_num = dec_num // 2
    return bin_num


dec_num = 7
print(decimal_to_binary(dec_num))


def binary_to_decimal(bin_num):
    dec_num = 0
    power = 0
    for i in reversed(str(bin_num)):
        dec_num = int(i) * (2 ** power)
        power += 1
    return dec_num

bin_num = 101
print(binary_to_decimal(bin_num))