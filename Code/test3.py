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

    def size(self):
        return len(self.items)


def evaluate_postfix(expression):
    """คำนวณผลลัพธ์ของนิพจน์ในรูปแบบ Postfix"""
    stack = Stack()
    
    # แยกนิพจน์ด้วยช่องว่าง
    for char in expression.split():
        if char.isdigit():  # ตรวจสอบว่าเป็นตัวเลข
            stack.push(int(char))
        elif char in "+-*/^":  # ตรวจสอบว่าเป็นตัวดำเนินการ
            if stack.size() < 2:
                raise ValueError("นิพจน์ไม่ถูกต้อง: มีตัวดำเนินการเกินจำนวนตัวเลขใน Stack")
            b = stack.pop()
            a = stack.pop()
            
            # คำนวณตามตัวดำเนินการ
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                if b == 0:
                    raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
                stack.push(a / b)
            elif char == '^':
                stack.push(a ** b)
        else:
            raise ValueError(f"พบตัวอักษรที่ไม่รู้จัก: '{char}'")
    
    # ตรวจสอบว่าเหลือข้อมูลใน Stack เพียง 1 ค่า
    if stack.size() != 1:
        raise ValueError("นิพจน์ไม่สมบูรณ์: เหลือตัวเลขใน Stack เกิน 1 ตัว")
    
    return stack.pop()


# โปรแกรมหลัก
if __name__ == "__main__":
    postfix_expression = input("Enter a Postfix expression (e.g., '5 1 2 + 4 * + 3 -'): ")
    try:
        result = evaluate_postfix(postfix_expression)
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
