def add(num):
    def number(num2):
        return num*num2
    print(number(3))
    return number
print(add(3))