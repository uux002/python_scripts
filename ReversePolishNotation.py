# _*_ coding:utf-8

class Stack(object):
    def __init__(self):
        self.stackList = []
        self.stackIndex = -1

    def IsEmpty():
        return (len(self.stackList) == 0)

    def Push(data):
        self.stackList.append(data)

    def Pop():
        if not IsEmpty():
            return self.stackList.pop()
        else:
            return None

    def Peek():
        if not IsEmpty():
            lastIndex = len(self.stackList) - 1
            return self.stackList[lastIndex]
        return None
    
    def Count():
        return len(self.stackList)
    

priorityDict = {'+':1,
                '-':1,
                '*':2,
                '/':2,
                '%':2,
                '(':3, }

# 是符号
def IsSymbol(symbol):
    if (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z') or (symbol >= '0' and symbol <= '9'):
        return True
    else:
        return False

# 是操作符
def IsOperation(symbol):
    if (symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '%'):
        return True
    return False

# 是左括号
def IsLeftBracket(symbol):
    if (symbol == '('):
        return True
    return False

# 是右括号
def IsRightBracket(symbol):
    if (symbol == ')'):
        return True
    return False

# A 的优先级是否高于 B
def IsHigherOrEqualPriority(symbolA,symbolB):
    priorityA = priorityDict.get(symbolA)
    priorityB = priorityDict.get(symbolB)
    if priorityA >= priorityB:
        return True
    return False


notationStack = Stack()
notationList = []

notations = "a+b*c+(d*e+f)*g"

for notation in notations:
    if IsSymbol(notation):
        notationList.append(notation)
    elif IsOperation(notation):
        while(True):
            topStackNotation = notationStack.Peek()
            if topStackNotation is None or IsLeftBracket(topStackNotation):
                notationStack.Push(notation)
                break
            elif IsHigherOrEqualPriority(topStackNotation,notation):
                topStackNotation = notationStack.Pop()
                notationList.append(topStackNotation)
    elif IsLeftBracket(notation):
        notationList.append(notation)
    elif IsRightBracket(notation):
        while(True):
            topStackNotation = notationStack.Peek()
            if topStackNotation is None or IsLeftBracket(topStackNotation):
                break
            else:
                topStackNotation.pop()
                notationList.append(topStackNotation)


for notation in notationList:
    print(notation)
            
    