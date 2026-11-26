#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""

    if not boxes:
        return True

    opened = {0}
    stack = [0]

    while stack:
        current = stack.pop()

        for key in boxes[current]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
