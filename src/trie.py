print("Hello World")
from typing import List
import collections

# A L I
# (n) A-> (n) L-> (n) I-> (y)


class Trie:
    def __init__(self):
        self._isEnd = False
        self._data = collections.defaultdict(Trie)

    def add_value(self, value) -> None:
        if not value:
            self._isEnd = True
            return

        self._data[value[0]].add_value(value[1:])

    # words:
    # ali, josh, alison, a

    # prefix: al -> ["ali", "alison"]

    def get_by_prefix(self, prefix) -> List[str]:

        def helper(trie, prefix, acc, results):
            if not prefix:
                for key, value in trie._data.items():
                    helper(value, prefix, acc + key,  results)

                if trie.isEnd:
                    results.append(acc)
                return

            acc += prefix[0]
            helper(trie._data[prefix[0]], prefix[1:], acc, results)



        result = []
        helper(self, prefix, '', result)
        return result

