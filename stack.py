# ID 64829423
import operator

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Невозможно выполнить операцию, стек пуст.')


OPERATORS = {
    '+': operator.add, 
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def calculator(lines, stack=None, converter=int, operators=OPERATORS):
    stack = Stack() if stack is None else stack
    for element in lines:
        if element in operators:
            element1, element2 = stack.pop(), stack.pop()
            stack.push(operators[element](element2, element1))
        else:
            try:
                stack.push(converter(element))
            except:
                raise ValueError(
                    f'Невозможно преобразовать "{element}" в '
                    f'{converter.__name__} или неподдерживаемая операция.')
    return stack.pop()


if __name__ == '__main__':
    try:
        print(calculator(input().split()))
    except(IndexError, ValueError) as err:
        print(err)
