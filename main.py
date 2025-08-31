#問題1
def say_hello():
    print('こんにちは！')
say_hello()
#問題2
def multiply_numbers(a,b):
    result=a*b
    return result
print(multiply_numbers(3,5))
#問題３
def greet_person(name,age):
    message=f"{name}と申します。年齢は{age}歳です."
    return message
print(greet_person("taji",25))


class Product:
    def __init__(self,name,stock):
        self.name=name
        self.stock=stock

    def add_stock(self,amount):
        self.stock +=amount

    def show_stock(self):
        print(f"{self.name}の在庫は{self.stock}個です")

item=Product("バナナ",5)
item.add_stock(5)
item.show_stock()


class TextEditor:
    def to_upper(self,text):
        return text.upper()
    
    def reverse_text(self,text):
        return text[::-1]
    
editor=TextEditor()

result1=editor.to_upper("Hello")
print(result1)

result2=editor.reverse_text("Hello")
print(result2)


    
