def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)
#
#tương đương với

#def printer(msg):
 #   print(msg)
#printer = star(percent(printer))
#Thứ tự mà chúng tôi trang trí chuỗi quan trọng. Nếu chúng tôi đã đảo ngược thứ tự như,

#@percent
#@star
#def printer(msg):
 #   print(msg)
#

printer("Hello")
