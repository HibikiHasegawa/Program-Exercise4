# my_module.py

def my_function():
    print("This is my function.")

class MyClass:
    def __init__(self):
        print("MyClass instance created.")

if __name__ == "__main__":
    # スクリプトが直接実行された場合に実行されるコード
    print("This script was run directly.")
    my_function()
    obj = MyClass()
