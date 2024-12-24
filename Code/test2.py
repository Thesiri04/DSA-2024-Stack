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


def decimal_to_base(decimal_number, base):
    """ฟังก์ชันแปลงเลขฐาน 10 ให้เป็นฐานใดๆ โดยใช้ Stack"""
    if base not in [2, 16]:
        raise ValueError("รองรับเฉพาะฐาน 2 และ 16 เท่านั้น")

    digits = "0123456789ABCDEF"  # ตัวเลขและตัวอักษรที่ใช้ในฐาน 16
    stack = Stack()
    
    # ตรวจสอบกรณีเลขศูนย์
    if decimal_number == 0:
        return "0"
    
    # คำนวณเลขฐาน
    while decimal_number > 0:
        remainder = decimal_number % base
        stack.push(remainder)
        decimal_number //= base
    
    # สร้างผลลัพธ์โดยนำตัวเลขออกจาก Stack
    converted_number = ""
    while not stack.is_empty():
        converted_number += digits[stack.pop()]
    
    return converted_number


# โปรแกรมหลัก
if __name__ == "__main__":
    decimal_input = int(input("Enter a decimal number: "))

    # แปลงเลขฐาน 10 เป็นฐาน 2
    binary_output = decimal_to_base(decimal_input, 2)
    print(f"Binary (Base 2): {binary_output}")

    # แปลงเลขฐาน 10 เป็นฐาน 16
    hex_output = decimal_to_base(decimal_input, 16)
    print(f"Hexadecimal (Base 16): {hex_output}")
