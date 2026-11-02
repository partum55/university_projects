"""
    Author: Nazar Mykhailyshchuk
    System for "Drunk Cherry"
"""

height = float(input())
weight = float(input())

max_volume = 5 * height * weight

crr = 0
alc = 0
crr_all = 0
volume = 0
amount = 0
temp = ""
percent = 0

while True:
    temp = ""
    n = input()

    if n == "U":
        try:
            percent = crr_all / volume
        except ZeroDivisionError:
            percent = 0
        finally:
            if percent > 0.15:
                print("Перевищено ліміт вишень")
                break
            else:
                crr = 0
                crr_all = 0
                alc = 0
                amount += volume
                volume = 0

    elif n == "q":
        try:
            percent = crr_all / volume
        except ZeroDivisionError:
            percent = 0
        finally:
            if percent > 0.15:
                print("Перевищено ліміт вишень")
            else:
                amount += volume
                print(amount)
            break

    elif n[0] == "0":
        if len(n) > 2:
            for i in range(2, len(n)):
                temp += n[i]
            crr = int(temp) * 5
            if crr + volume > 500:
                print("Збій роботи датчика")
                break
            elif crr + volume > max_volume:
                print("Перевищено ліміт алкоголю")
                break
            else:
                crr_all += crr
                volume += crr
                crr = 0
        else:
            crr += 5
            if crr + volume > 500:
                print("Збій роботи датчика")
                break
            elif crr + amount > max_volume:
                print("Перевищено ліміт алкоголю")
                break
            else:
                crr_all += crr
                volume += crr
                crr = 0

    elif n[0] == "#":
        if len(n) > 2:
            for i in range(2, len(n)):
                temp += n[i]
            alc = int(temp) * 20
            if alc + volume > 500:
                print("Збій роботи датчика")
                break
            elif alc + amount + volume > max_volume:
                print("Перевищено ліміт алкоголю")
                break
            else:
                volume += alc
                alc = 0
        else:
            alc += 20
            if alc + volume > 500:
                print("Збій роботи датчика")
                break
            elif alc + amount + volume > max_volume:
                print("Перевищено ліміт алкоголю")
                break
            else:
                volume += alc
                alc = 0
