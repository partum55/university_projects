"""_summary_
avarage grade
"""

grade = 0

for i in range(5):
    a = int(input())
    grade += a
    if (a < 0) or (a > 100):
        print("None)")
        break
else:
    grade = grade / 5
    print(f"Average grade = {sum} -> ", end = "")
    if 90 <= grade<= 100:
        print ("А")
    elif 80 <= grade < 90:
        print ("B")
    elif 75 <= grade < 80:
        print ("C")
    elif 65 <= grade < 75:
        print ("D")
    elif 60 <= grade < 65:
        print ("E")
    else:
        print("F")
