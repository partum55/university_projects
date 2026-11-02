def happy_number(number: int) -> bool | None:
    if not isinstance(number, int):
        return None
    number = f"{number:0{8}}"
    num1, num2 = number[:4], number[4:]
    while True:
        if len(num1) == 1 and len(num2) == 1:
            break
        sum1, sum2 = 0, 0
        for i in num1:
            sum1 += int(i)
        for i in num2:
            sum2 += int(i)
        if sum1 == sum2:
            return True
        num1, num2 = f"{sum1}", f"{sum2}"
print(happy_number(159123))