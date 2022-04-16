from __future__ import annotations


class Node:
    def __init__(self, j: int, name: str):
        self.i = j
        self.name_of_node = name
        # print(j)
        self.left = None
        self.right = None

    def add_node(self, node_var: Node):
        if node_var.i <= self.i:
            if self.left is None:
                self.left = node_var
            else:
                self.left.add_node(node_var)
        else:
            if self.right is None:
                self.right = node_var
            else:
                self.right.add_node(node_var)

    def __str__(self):
        if self.left is None and self.right is None:
            return f'{self.i}'
        elif self.left is None:
            return f'{self.i} <= {self.right}'
        elif self.right is None:
            return f'{self.left} <= {self.i}'
        return f'({self.left.__str__()} <= {self.i} <= {self.right})'
