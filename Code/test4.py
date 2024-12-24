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


def is_valid_json(json_string):
    """ตรวจสอบความถูกต้องของ JSON string โดยใช้ Stack"""
    stack = Stack()
    opening_brackets = "{[\""
    closing_brackets = "}]\"," 
    matching_brackets = {')': '(', '}': '{', ']': '[', '\"': '\"'}

    in_string = False  # ตัวแปรสำหรับตรวจสอบว่าอยู่ใน string หรือไม่

    for char in json_string:
        if char == '"' and (stack.is_empty() or stack.peek() != '"'):
            # เริ่มต้นหรือจบ string
            stack.push(char)
            in_string = not in_string
        elif char == '"' and stack.peek() == '"':
            stack.pop()
            in_string = not in_string
        elif in_string:
            # ข้ามการตรวจสอบตัวอักษรภายใน string
            continue
        elif char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False

    # หาก stack ว่างแสดงว่าคำสั่ง JSON ถูกต้อง
    return stack.is_empty()


# โปรแกรมหลัก
if __name__ == "__main__":
    json_string = input("Enter a JSON string to validate: ")
    try:
        if is_valid_json(json_string):
            print("The JSON string is valid.")
        else:
            print("The JSON string is invalid.")
    except ValueError as e:
        print(f"Error: {e}")
