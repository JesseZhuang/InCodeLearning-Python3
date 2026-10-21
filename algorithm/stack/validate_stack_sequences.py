class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_index = 0

        for value in pushed:  # O(n) pushes.
            stack.append(value)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()  # Each value is popped at most once: O(n) total.
                pop_index += 1
                if pop_index == len(popped):
                    return True

        return pop_index == len(popped)  # O(n) auxiliary stack space.
