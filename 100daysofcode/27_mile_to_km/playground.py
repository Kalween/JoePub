# def add(*args):
#     total = 0
#     for i in args:
#         total += i
#     print(total)

# add(1,2,3,1,2,19)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)