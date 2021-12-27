from typing import Generic, List, TypeVar

T = TypeVar("T")


class BinaryTreeNode(Generic[T]):
    def __init__(
        self,
        value: T,
        left_child: "BinaryTreeNode[T]" = None,
        right_child: "BinaryTreeNode[T]" = None,
    ) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree(Generic[T]):
    def __init__(self, root: BinaryTreeNode[T]) -> None:
        self._root = root

    @classmethod
    def from_traversals(
        cls, pre_order_traversal: List[T], in_order_traversal: List[T]
    ) -> "BinaryTree[T]":
        pass

    def in_order_traversal(self) -> List[T]:
        traversal: List[T] = list()

        if self._root.left_child:
            traversal.extend(BinaryTree(self._root.left_child).in_order_traversal())

        traversal.append(self._root.value)

        if self._root.right_child:
            traversal.extend(BinaryTree(self._root.right_child).in_order_traversal())

        return traversal

    def pre_order_traversal(self) -> List[T]:
        traversal: List[T] = list()

        traversal.append(self._root.value)

        if self._root.left_child:
            traversal.extend(BinaryTree(self._root.left_child).pre_order_traversal())

        if self._root.right_child:
            traversal.extend(BinaryTree(self._root.right_child).pre_order_traversal())

        return traversal

    def post_order_traversal(self) -> List[T]:
        traversal: List[T] = list()

        if self._root.left_child:
            traversal.extend(BinaryTree(self._root.left_child).post_order_traversal())

        if self._root.right_child:
            traversal.extend(BinaryTree(self._root.right_child).post_order_traversal())

        traversal.append(self._root.value)

        return traversal
