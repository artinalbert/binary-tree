from binary_tree import Node


def main():
    root = Node(6, 'root_node')
    print(root)
    child = Node(5, 'second_node')
    root.add_node(child)
    # child.add_node(root)
    print(root)
    child2 = Node(9, 'child2_node')
    root.add_node(child2)
    print(root)
    child3 = Node(99, 'child3_node')
    root.add_node(child3)
    print(root)
    child4 = Node(4, 'child4')
    root.add_node(child4)
    print(root)


if __name__ == '__main__':
    main()
