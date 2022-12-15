import random
import string
import time

list_items = string.ascii_letters + " "
user_input = str(input("Enter the text you want to write: "))
txt_wri = user_input + " "
i = 0
new_txt = ""
count = 0

while i in range(0, len(txt_wri)):
    a = random.choice(list_items)
    if new_txt.__contains__(user_input):
        print("\r", new_txt)
        print("Number of steps: " + str(count))
        break
    elif a == txt_wri[i]:
        new_txt = new_txt + txt_wri[i]
        time.sleep(0.01)
        i = i + 1
        count = count + 1
    else:
        if i > 0:
            print("\r", new_txt + a, end="")
            time.sleep(0.003)
            count = count + 1
        else:
            print("\r", a, end="")
            time.sleep(0.005)
            count = count + 1
