class MyClass:
    '''A simple class with some attributes and methods.'''
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"
    def method1(self):
        return "This is method1"
    def method2(self):
        return "This is method2"

def main():
    obj = MyClass()
    print("Attributes and methods of MyClass:")    
    #print(dir(obj))
    

if __name__ == "__main__":
    main()
    my_obj = MyClass()
    print(my_obj.__class__)
    