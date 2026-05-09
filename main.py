class Mixin:
    def __init__(self):
        self.mixin_name = "Mixin"

    def mixin_method(self):
        return "Mixin method"

class ClassA(Mixin):
    def __init__(self):
        super().__init__()
        self.class_a_name = "Class A"

    def class_a_method(self):
        return "Class A method"

class ClassB(Mixin):
    def __init__(self):
        super().__init__()
        self.class_b_name = "Class B"

    def class_b_method(self):
        return "Class B method"

class ClassC(ClassA, ClassB):
    def __init__(self):
        super().__init__()

    def class_c_method(self):
        return "Class C method"

obj = ClassC()
print(obj.mixin_name)  # Mixin
print(obj.mixin_method())  # Mixin method
print(obj.class_a_name)  # Class A
print(obj.class_a_method())  # Class A method
print(obj.class_b_name)  # Class B
print(obj.class_b_method())  # Class B method
print(obj.class_c_method())  # Class C method
