"""_summary_
    не сварись будь ласка
"""

capticy = float(input())
cent_done = 0
pere_done = 0
all_k = -1
summary = 0

while True:
    all_k += 1
    try:
        box = input()
        box = float(box)
        if box <= 0:
            raise ValueError
    except ValueError:
        if box == "q":
            break
        pere_done += 1
    else:
        if summary + box <= capticy:
            cent_done += 1
            summary += box

print(cent_done)
print(pere_done)
print(all_k - cent_done - pere_done)
