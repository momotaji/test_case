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

