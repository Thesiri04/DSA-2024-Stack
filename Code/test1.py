class Stack:
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

def reverse_string(input_string):
    """ฟังก์ชันสำหรับกลับลำดับตัวอักษรโดยใช้ Stack"""
    stack = Stack()
    
    # Push ตัวอักษรแต่ละตัวลงใน Stack
    for char in input_string:
        stack.push(char)
    
    # Pop ตัวอักษรจาก Stack และสร้างข้อความใหม่
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# รับข้อความจากผู้ใช้
user_input = input("Enter a string to reverse: ")
reversed_output = reverse_string(user_input)
print(f"Reversed string: {reversed_output}")
