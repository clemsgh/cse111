import math

items = int(input("What is the number of items? "))
boxes = int(input("How many items fit in a box? "))

num_boxes = math.ceil(items / boxes)

print(f"/n For {items} items, packing {boxes}"
    f" items in each box, you will need {num_boxes} boxes.")