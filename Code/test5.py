class Stack:
    """คลาสสำหรับจัดการ Stack"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")


def precedence(op):
    """ฟังก์ชันที่ใช้คืนค่าความสำคัญของตัวดำเนินการ"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def apply_operation(a, b, op):
    """ฟังก์ชันที่ใช้คำนวณตัวดำเนินการ"""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '^':
        return a ** b
    raise ValueError(f"Unknown operator: {op}")


def evaluate_infix(expression):
    """ฟังก์ชันสำหรับประเมินผลนิพจน์ Infix"""
    values = Stack()  # Stack สำหรับเก็บตัวเลข
    operators = Stack()  # Stack สำหรับเก็บตัวดำเนินการ

    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            # อ่านตัวเลขแบบต่อเนื่อง (เช่น 123)
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)
            i -= 1  # ลด i เพราะ while ด้านนอกจะเพิ่ม 1 อยู่แล้ว
        elif char == '(':
            operators.push(char)
        elif char == ')':
            while not operators.is_empty() and operators.peek() != '(':
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_operation(a, b, op))
            operators.pop()  # เอาวงเล็บเปิด '(' ออกจาก Stack
        elif char in '+-*/^':
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(char)):
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_operation(a, b, op))
            operators.push(char)
        i += 1

    # ประมวลผลตัวดำเนินการที่เหลือใน Stack
    while not operators.is_empty():
        op = operators.pop()
        b = values.pop()
        a = values.pop()
        values.push(apply_operation(a, b, op))

    return values.pop()


# โปรแกรมหลัก
if __name__ == "__main__":
    expression = input("Enter an Infix expression to evaluate: ")
    try:
        result = evaluate_infix(expression.replace(" ", ""))
        print(f"The result of the expression is: {result}")
    except Exception as e:
        print(f"Error: {e}")
