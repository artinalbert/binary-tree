from __future__ import annotations


class Node:
    def __init__(self, value: int, name_of_node: str):
        self.value = value
        self.name_of_node = name_of_node
        # print(j)
        self.left = None
        self.right = None

    def add_node(self, node_var: Node):
        if node_var.value <= self.value:
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
            return f'{self.value}'
        elif self.left is None:
            return f'{self.value} <= {self.right}'
        elif self.right is None:
            return f'{self.left} <= {self.value}'
        return f'({self.left.__str__()} <= {self.value} <= {self.right})'
