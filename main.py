
import math

with open("starttxt.txt", "r", encoding="utf-8") as file:
    intro = file.read()


def press_enter():
    input()


print(intro)
press_enter()
print("test")

chose