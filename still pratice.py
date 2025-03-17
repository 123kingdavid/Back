# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")


# hello("Hello","Mr","king davis", "desmond",)

      

# def get_phone(country,area,first,last):
#     return f"{country} -{area} - {first} - {last}"

# phone_num = get_phone(country= 2, area= 234, first=231,last= 7201,)

# print(phone_num) 

# args: allows you to pass multiple non key arguments
# kwargs: allows you to pass multiple keyword arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3 4,)):  