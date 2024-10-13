#!/usr/bin/python3
def canUnlockAll(boxes):
    # Use a set to track opened boxes
    opened_boxes = set()
    # Start with the first box
    opened_boxes.add(0)
    # Initialize a queue with the first box
    queue = [0]
    
    while queue:
        # Get the current box number
        current_box = queue.pop(0)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # Check if the key opens a box that has not been opened yet
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)
    
    # Check if we have opened all the boxes
    return len(opened_boxes) == len(boxes)

# Example usage:
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
