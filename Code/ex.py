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
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        return len(self.items)

# Create a stack
stack = Stack()

# 1. รับเลขจากผู้ใช้เพื่อเพิ่มใน Stack
print("Enter 5 numbers to push into the stack:")
for _ in range(5):
    num = int(input("Enter a number: "))
    stack.push(num)
print(f"\nStack after push: {stack.items}")

# 2. แสดงข้อมูลบนสุดด้วย peek
print("\nTop element using peek:")
top = stack.peek()
print(f"Top element: {top}")

# 3. นำข้อมูลออกจาก Stack 3 ตัวด้วย pop
print("\nRemoving 3 elements using pop:")
for _ in range(3):
    print(f"Popped element: {stack.pop()}")
print(f"\nStack after pop: {stack.items}")

# 4. แสดงข้อมูลที่เหลือใน Stack
print("\nRemaining elements in the stack:")
print(f"Stack: {stack.items}")
