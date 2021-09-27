from stack.Stack import Stack


class InfixToPostfix:
    OPERATORS = {'^': 1, '*': 2, '/': 2, '+': 3, '-': 3}    # 'sin': 0, 'cos': 0,

    def _parser(self, string):
        numbers = "1234567890."
        number = ""
        self.input = string.replace(" ", "")
        print(self.input)
        tokens = []
        for i in self.input:
            if i in numbers:
                number += i
            elif len(number) != 0:
                tokens.append(number)
                number = ""
            if i in self.OPERATORS or i in '(' or i in ')':
                tokens.append(i)
            elif i == 'o':
                tokens.append('cos')
            elif i == 'i':
                tokens.append('sin')
        return tokens

    def __init__(self, string):
        self._tokens = self._parser(string)
        self._stack_of_operators = Stack([])

    def print_tokens(self):
        """
        for debugging
        :return:
        """
        print(self._tokens)

    def _shunting_yard(self):
        result = ""
        for token in self._tokens:
            if token.isdigit():
                result += token + " "
            elif token == 'sin':
                self._stack_of_operators.pushback('sin')
            elif token == 'cos':
                self._stack_of_operators.pushback('cos')
            elif token in self.OPERATORS:
                pass

