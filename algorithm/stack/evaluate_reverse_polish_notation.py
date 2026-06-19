"""LeetCode 150, medium, tags: array, math, stack."""


class Solution:
    """Stack approach. Process tokens left to right, push operands, pop+apply for operators."""

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []  # O(n) space
        for token in tokens:  # O(n) time
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))  # truncate toward zero
                case _:
                    stack.append(int(token))
        return stack[0]
