import pytest

from data_structure_implementation.binary_tree import BinaryTree, BinaryTreeNode


class TestBinaryTree:
    @pytest.fixture
    def gen_tree(self) -> BinaryTree[int]:

        root = BinaryTreeNode(
            25,
            BinaryTreeNode(
                15,
                BinaryTreeNode(10, BinaryTreeNode(4), BinaryTreeNode(12)),
            ),
            BinaryTreeNode(
                50,
                BinaryTreeNode(35, BinaryTreeNode(31), BinaryTreeNode(44)),
                BinaryTreeNode(70, None, BinaryTreeNode(88)),
            ),
        )

        return BinaryTree(root)

    def test_in_order_traversal(self, gen_tree: BinaryTree[int]):
        in_order_traversal = [4, 10, 12, 15, 25, 31, 35, 44, 50, 70, 88]
        assert gen_tree.in_order_traversal() == in_order_traversal

    def test_pre_order_traversal(self, gen_tree: BinaryTree[int]):
        pre_order_traversal = [25, 15, 10, 4, 12, 50, 35, 31, 44, 70, 88]
        assert gen_tree.pre_order_traversal() == pre_order_traversal

    def test_post_order_traversal(self, gen_tree: BinaryTree[int]):
        post_order_traversal = [4, 12, 10, 15, 31, 44, 35, 88, 70, 50, 25]
        assert gen_tree.post_order_traversal() == post_order_traversal

    @pytest.mark.skip(reason="not implemented yet")
    def test_from_traversals(self):
        pre_order_traversal = [25, 15, 10, 4, 12, 50, 35, 31, 44, 70, 88]
        in_order_traversal = [4, 10, 12, 15, 25, 31, 35, 44, 50, 70, 88]

        tree = BinaryTree.from_traversals(pre_order_traversal, in_order_traversal)

        assert tree.pre_order_traversal() == pre_order_traversal
        assert tree.in_order_traversal() == in_order_traversal
