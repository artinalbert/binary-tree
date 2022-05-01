from binary_tree.binary_tree import Node

def test_binary_tree():
    node_1 = Node(66, "node 1")
    assert node_1.name_of_node == "node 1"
    assert node_1.value == 66
    node_2 = Node(65, "node2")
    assert node_1.add_node(node_2) is None
    assert node_1.left == node_2
    assert str(node_1) == '65 <= 66'

