# snake.py
class Node:
    def __init__(self, position):
        self.position = position
        self.next = None

class Snake:
    def __init__(self, initial_position):
        self.head = Node(initial_position)
        self.length = 1
        self.direction = (0, -1)  # Start moving up
        self.grow = False  # New attribute to manage growth

    def move(self):
        # Add a new head in the current direction
        new_position = (self.head.position[0] + self.direction[0] * 20,
                        self.head.position[1] + self.direction[1] * 20)
        new_head = Node(new_position)
        new_head.next = self.head
        self.head = new_head

        # Check if we should grow
        if not self.grow:
            # Remove the tail to maintain length
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None  # Remove tail node
        else:
            # Reset grow after growing by one node
            self.grow = False

    def grow_snake(self):
        self.grow = True  # Trigger growth on next move

    def change_direction(self, direction):
        self.direction = direction
