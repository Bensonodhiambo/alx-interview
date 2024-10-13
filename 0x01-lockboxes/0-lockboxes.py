#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): Each list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    opened_boxes = set()  # Track opened boxes
    opened_boxes.add(0)   # Start by opening the first box
    queue = [0]           # Initialize queue with the first box

    while queue:
        current_box = queue.pop(0)
        # Check the keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)  # Mark box as opened
                queue.append(key)       # Add to queue to explore its keys

    return len(opened_boxes) == len(boxes)  # Check if all boxes are opened
