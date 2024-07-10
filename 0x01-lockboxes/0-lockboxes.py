#!/usr/bin/env python3


def canUnlockAll(boxes):
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
