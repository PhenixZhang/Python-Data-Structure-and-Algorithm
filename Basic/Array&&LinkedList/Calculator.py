class Calculator(object):

    def __init__(self):
        # 操作符集合
        self.operators = ['+', '-', '*', '/', '(', ')']
        # 操作符优先级
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 3,
            ')': 3
        }

    def generate_postfix_expression(self, expression):
        """
        生成后缀表达式
        :param expression:
        :return:
        """

        # 去除表达式中所有空格
        expression = expression.replace(' ', '')

        exprelst = []
        temp = ''
        for i,each in enumerate(expression):
            if each.isdigit() or each == '.':
                temp += each
                if i == len(expression)-1:
                    exprelst.append(temp)
            else:
                if len(temp)>0:
                    exprelst.append(temp)
                    temp = ''
                exprelst.append(each)

        expression = exprelst

        # 创建list作为栈，list的append和pop方法刚好和栈的入栈和出栈方法相同
        # 操作符栈
        operator_stack = list()
        # 后缀表达式是从尾部插入数据，使用后缀表达式计算结果是从头开始遍历，可以理解为先进先出，可以使用队列实现，
        # 这里为了简便用list代替，不做内存释放处理
        expression_stack = list()

        for element in expression:
            # 如果是数字则直接入表达式栈
            if element in self.operators:

                # 如果栈为空，操作符直接入操作符栈，或者为左括号，也直接入操作符栈
                if not operator_stack:
                    operator_stack.append(element)
                else:
                    # 如果目标元素是右括号，操作符栈顶出栈直接遇到左括号，且出栈的操作符除了括号入到表达式队列中
                    if element == ')':
                        for top in operator_stack[::-1]:
                            if top != '(':
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.pop()
                                break
                    else:
                        for top in operator_stack[::-1]:
                            # 如果目标元素大于栈顶元素，则直接入栈，否则栈顶元素出栈，入到表达式队列中
                            # 左括号只有遇到右括号才出栈
                            if self.priority[top] >= self.priority[element] and top != '(':
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.append(element)
                                break

                        # 可能操作符栈所有的元素优先级都大于等于目标操作符的优先级，这样的话操作符全部出栈了，
                        # 而目标操作符需要入栈操作
                        if not operator_stack:
                            operator_stack.append(element)

            else:
                expression_stack.append(element)

        # 中缀表达式遍历结束，操作符栈仍有操作符，将操作符栈中的操作符入到表达式栈中
        for i in range(len(operator_stack)):
            expression_stack.append(operator_stack.pop())

        return expression_stack

    def calcaulate(self, expression):
        # 生成后缀表达式
        expression_result = self.generate_postfix_expression(expression)
        # 使用list作为栈来计算
        calcalate_stack = list()

        # 遍历后缀表达式
        for element in expression_result:
            # 如果为数字直接入栈
            # 遇到操作符，将栈顶的两个元素出栈
            if element not in self.operators:
                calcalate_stack.append(element)
            else:
                # 操作数
                number1 = calcalate_stack.pop()
                # 被操作数
                number2 = calcalate_stack.pop()
                # 结果 =  被操作数 操作符 操作数 （例：2 - 1）
                result = self.operate(number1, number2, element)
                # 计算结果入栈
                calcalate_stack.append(result)

        ret = calcalate_stack[0]
        if int(ret) == ret:
            ret = int(ret)
        return ret

    def operate(self, number1, number2, operator):
        """
        计算结果
        :param number1: 操作数
        :param number2: 被操作数
        :param operator: 操作符
        :return:
        """
        number1 = float(number1)
        number2 = float(number2)

        if operator == '+':
            return number2 + number1
        if operator == '-':
            return number2 - number1
        if operator == '*':
            return number2 * number1
        if operator == '/':
            return number2 / number1


if __name__ == '__main__':
    c = Calculator()
    expression = '2.1 + (3 - 1)*3 + 8 / 4'
    expression_result = c.calcaulate(expression)
    print(expression_result)

