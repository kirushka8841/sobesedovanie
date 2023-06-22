balanced_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
unbalanced_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True # вложенный is_empty — проверка стека на пустоту. Метод возвращает True или False;

    def push(self, item):
        self.stack.append(item) # добавляет новый элемент на вершину стека. Метод ничего не возвращает;

    def pop(self):
        if len(self.stack) == 0:
            return None 
        removed = self.stack.pop()
        return removed # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0] # возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
        
    def size(self):
        return len(self.stack) #возвращает количество элементов в стеке.
    
    def check_list(string):
        stack_list = []
        for element in string:
            if element in '{([':
                stack_list.append(element)
            elif element in '})]':
                if not stack_list:
                    return 'Несбалансировано'
                if element == ')' and stack_list[-1] == '(':
                    stack_list.pop()
                elif element == '}' and stack_list[-1] == '{':
                    stack_list.pop()
                elif element == ']' and stack_list[-1] == '[':
                    stack_list.pop()
                else:
                    return 'Несбалансировано'
        if not stack_list:
            return 'Сбалансировано'
        else:
            return 'Несбалансировано'

if __name__ == '__main__':
    for string in balanced_list:
        print(Stack.check_list(string))
    for string in unbalanced_list:
        print(Stack.check_list(string))