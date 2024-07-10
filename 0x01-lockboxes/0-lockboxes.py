#!/usr/bin/python3
"""
Determine if all boxes can be opened.

Args:boxes (list of lists): A list where each element is a list of keys
contained in a box.

Returns:bool: True if all boxes can be opened, otherwise False.
"""


def canUnlockAll(boxes):
    """ function to unlock all boxes """
    open_boxes = set()
    open_boxes.add(0)
    queue = [0]

    while queue:
        curr_box = queue.pop(0)
        for key in boxes[curr_box]:
            if key not in open_boxes and key < len(boxes):
                open_boxes.add(key)
                queue.append(key)

    return len(open_boxes) == len(boxes)
