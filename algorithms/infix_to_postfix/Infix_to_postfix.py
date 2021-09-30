from stack.Stack import Stack


class InfixToPostfix:
    OPERATORS = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 'sin': 0, 'cos': 0,

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
        if len(number) != 0:
            tokens.append(number)
        return tokens

    def __init__(self, string):
        self._tokens = self._parser(string)
        print(self._tokens)
        # self._stack_of_operators = Stack([])

    def print_tokens(self):
        """
        for debugging
        :return:
        """
        print(self._tokens)

    def _pop_operators(self, token):
        output = ""
        while True:
            op2 = str(self._stack_of_operators.last_elem)
            # print(f"output {output}")
            # print(f"stack: {self._stack_of_operators}")
            if op2 is None or not (op2 in self.OPERATORS.keys()):
                # print(op2 not in self.OPERATORS, " second")
                # print(op2 is None, " first")
                self._stack_of_operators.pushback(token)
                print("stack: ", self._stack_of_operators)
                print("output: ", output)
                return output
            elif self.OPERATORS[op2] > self.OPERATORS[token] or \
                 (self.OPERATORS[op2] == self.OPERATORS[token] and token != '^'):
                output += str(self._stack_of_operators.pop()) + " "
            else:
                self._stack_of_operators.pushback(token)
                print("stack: ", self._stack_of_operators)
                print("output: ", output)
                return output

    def _pop_bracket(self):
        output = ''
        while str(self._stack_of_operators.last_elem) != '(':
            if self._stack_of_operators.last_elem is not None:
                output += str(self._stack_of_operators.pop()) + " "
            else:
                raise ValueError("incorrect sequence of brackets")
        self._stack_of_operators.pop()
        return output

    def _shunting_yard(self):
        result, flag = "", 0
        for token in self._tokens:
            print(token)
            if token.isdigit():
                result += token + " "
            elif token == 'sin':
                self._stack_of_operators.pushback('sin')
            elif token == 'cos':
                self._stack_of_operators.pushback('cos')
            elif token in self.OPERATORS:
                if flag == 0:
                    self._stack_of_operators = Stack(token)
                    print(f"stack): {self._stack_of_operators}, token is {token}")
                    flag = 1
                else:
                    result += self._pop_operators(token)
            elif token == '(':
                self._stack_of_operators.pushback('(')
            elif token == ')':
                print('stack before ): ', self._stack_of_operators)
                result += self._pop_bracket() + " "
        while self._stack_of_operators.last_elem is not None:
            result += str(self._stack_of_operators.pop()) + " "
        return result

    def start(self):
        result = self._shunting_yard()
        print(result)
        print(f"\n\nstack {self._stack_of_operators}")
        return result
