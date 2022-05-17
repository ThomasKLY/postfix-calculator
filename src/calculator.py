from typing import List


class Calculator:
    def __init__(self):

        self.operators = {"+", "-", "*", "/", "%"}

    def __compute(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Divisor can't be 0 for / operator")
            return a // b
        elif operator == "%":
            if b == 0:
                raise ValueError("Divisor can't be 0 for / operator")
            return a % b

    def __postfix(self, tokens: List[str]) -> int:
        memory = []
        for token in tokens:
            if token in self.operators:
                b = memory.pop()
                a = memory.pop()
                ans = self.__compute(a, b, token)
            elif token.isdigit():
                ans = int(token)
            else:
                raise ValueError(
                    f"Received {token} as input, "
                    f"the input can only a be whole number or one of the following operands: "
                    f"{', '.join(self.operators)}"
                )

            memory.append(ans)

        if len(memory) == 1:
            return memory.pop()
        else:
            raise ValueError()

    def __infix(self, tokens: List[str]) -> int:
        postfix_tokens = self.__infix_to_postfix(tokens)
        return self.__postfix(postfix_tokens)

    def __infix_to_postfix(self, tokens: List[str]) -> List[str]:
        raise NotImplementedError()

    def __tokenize(self, expression: str):
        return expression.split(" ")

    def calc(self, expression: str, method="postfix") -> int:
        tokens = self.__tokenize(expression)
        if len(tokens) == 0:
            raise ValueError("Empty input detected")

        if method == 'postfix':
            return self.__postfix(tokens)
        elif method == 'infix':
            return self.__infix(tokens)
        else:
            raise ValueError('Calculator method can only be either postfix or infix')
